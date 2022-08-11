import bpy
from bpy.types import Gizmo, GizmoGroup, bpy_prop_collection
from mathutils import Matrix, Vector

from .gizmo_config import gizmo_colors

def dpi_factor() -> float:
  systemPreferences = bpy.context.preferences.system
  retinaFactor = getattr( systemPreferences, "pixel_size", 1 )
  return int( systemPreferences.dpi * retinaFactor ) / 72

##
# GizmoSet
#   - single-state
#     - one icon
#     - one action
#     - possible toggle by variable state
# 
#   - 2-state (boolean)
#     - 2 icons
#     - 2 actions (or 1 action for both icons)
# 
##

class GizmoSet:
  group: GizmoGroup;
  
  def setup(self, group:GizmoGroup, config: dict ):
    self.visible = True
    self.config = config
    self.has_dependent = 'has_dependent' in config or False
    self.group = group
    self.scale =  config['scale'] if ('scale' in config) else 14
    self.binding = config['binding']
    self.has_attribute_bind = self.binding['attribute'] if 'attribute' in self.binding else False
    self.primary = self.__buildGizmo( config['command'], config['icon'] )

  def __getSettings( self ):
    return bpy.context.preferences.addons[ 'touchview' ].preferences

  def draw_prepare(self):
    settings = self.__getSettings()
    self.hidden = not settings.show_menu
    self.skip_draw = False
    self.__updatevisible()

    if self.binding['name'] == 'float_menu':
      self.primary.hide = not settings.show_float_menu
    if self.binding['name'] in ['menu_controller']:
      self.primary.hide = 'float' not in settings.menu_style or not settings.show_menu
    if self.binding['name'] in ['menu_controller', 'float_menu']:
      gui_scale = 22 * dpi_factor()
      self.primary.scale_basis = max( settings.menu_spacing - gui_scale/1.5, gui_scale/2)

  def move(self, position: Vector):
    self.primary.matrix_basis = Matrix.Translation(position) 

  def __updatevisible(self):
    if not self.__getSettings().show_menu and self.binding['name'] not in ['float_menu']:
      self.visible = False
      self.primary.hide = True
      return
    if(self.binding['location'] == "prefs"):
      self.visible = getattr(
        bpy.context.preferences.addons["touchview"].preferences,
        'show_'+self.binding['name']
      ) and self.binding['name'] in self.__getSettings().getGizmoSet( bpy.context.mode )

    if self.visible:
      self.visible = self.__visibilityLock() and not self.__checkAttributeBind()
    self.primary.hide = not self.visible

  def __visibilityLock(self) -> bool:
    if self.__getSettings().menu_style == 'fixed.bar':
      return True
    return not self.hidden

  # if an attribute being assigned to active_object should hide/show Gizmo 
  def __checkAttributeBind(self):
    if not self.has_attribute_bind:
      return False
    bind = self.binding['attribute']
    state = self.__findAttribute(bind['path'], bind['value']) == bind['state']
    return not state

  # search for attribute, value through context.
  # will traverse bpy_prop_collection entries by next attr to value comparison
  def __findAttribute(self, path: str, value: any):
    names = path.split( "." )
    current = bpy.context
    for i, prop in enumerate( names ):
        current = getattr( current, prop )
        if current == None:
            return False 

        if isinstance( current, bpy_prop_collection ):
            item = ''
            for item in current:
                if getattr(item, names[i+1]) == value:
                    return True
            return False
    return getattr(current, value) 

  # initialize each gizmo, add them to named list with icon name(s)
  def __buildGizmo( self, command: str, icon: str ) -> Gizmo:
    gizmo = self.group.gizmos.new( "GIZMO_GT_button_2d" )
    gizmo.target_set_operator( command )
    gizmo.icon = icon
    gizmo.use_tooltip = False
    gizmo.use_event_handle_all = True
    gizmo.use_grab_cursor = True if 'use_grab_cursor' in self.config else False
    gizmo.line_width = 5.0
    gizmo.use_draw_modal = True
    gizmo.draw_options = { 'BACKDROP', 'OUTLINE' }
    self.__setColors( gizmo )
    gizmo.scale_basis = self.scale or 14
    return gizmo

  def __setColors(self, gizmo: Gizmo):
    gizmo.color = gizmo_colors[ "active" ][ "color" ]
    gizmo.color_highlight = gizmo_colors[ "active" ][ "color_highlight" ]
    gizmo.alpha = gizmo_colors[ "active" ][ "alpha" ]
    gizmo.alpha_highlight = gizmo_colors[ "active" ][ "alpha_highlight" ]


class GizmoSetBoolean( GizmoSet ):
  def setup(self, group:GizmoGroup, config: dict ):
    self.visible = True
    self.config = config
    self.has_dependent = 'has_dependent' in config or False
    self.group = group
    self.scale =  config['scale'] if ('scale' in config) else 14
    self.binding = config['binding']
    self.has_attribute_bind = self.binding['attribute'] if 'attribute' in self.binding else False
    self.onGizmo = self._GizmoSet__buildGizmo( config['command'], config['onIcon'] )
    self.offGizmo = self._GizmoSet__buildGizmo( config['command'], config['offIcon'] )
    self.__setActiveGizmo(True)

  def __setActiveGizmo(self, state: bool):
    self.onGizmo.hide = True
    self.offGizmo.hide = True
    self.primary = self.onGizmo if state else self.offGizmo

  def draw_prepare(self):
    settings = self._GizmoSet__getSettings()
    self.hidden = not settings.show_menu
    self.skip_draw = False
    self.__updatevisible()

  def __updatevisible(self):
    if not self._GizmoSet__getSettings().show_menu and self.binding['name'] not in ['float_menu']:
      self.visible = False
      self.primary.hide = True
      return
    self.visible = getattr(bpy.context.preferences.addons["touchview"].preferences, 'show_'+self.binding['name']);
    if self.visible:
      self.visible = self._GizmoSet__visibilityLock() and not self._GizmoSet__checkAttributeBind()

    bind = self.binding
    self.__setActiveGizmo(self._GizmoSet__findAttribute(bind['location'], bind['name']))
    self.primary.hide = not self.visible


class GizmoSetEnum( GizmoSet ):
    gizmos: list[Gizmo]
    def setup(self, group:GizmoGroup, config):
      pass
