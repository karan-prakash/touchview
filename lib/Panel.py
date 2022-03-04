import bpy
from bpy.types import Context, Panel, Menu


class VIEW3D_PT_NendoPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NENDO"


class VIEW3D_PT_NendoViewport(VIEW3D_PT_NendoPanel, Panel):
    bl_idname = "VIEW3D_PT_view_ops"
    bl_label = "Viewport Settings"

    def draw(self, context):
        settings = bpy.context.preferences.addons['touchview'].preferences
        view = context.space_data
        space = context.area.spaces.active

        col = self.layout.column()
        col.label(text="Control Zones")
        col.prop(settings, "is_enabled", text="Enable")
        col.prop(settings, "swap_panrotate")
        col.prop(settings, "isVisible", text="Show Overlay")
        col.prop(settings, "use_multiple_colors")
        col.prop(settings, "overlay_main_color", text="Main Color")
        if settings.use_multiple_colors:
            col.prop(settings, "overlay_secondary_color", text="Secondary Color")
        col.prop(settings, "width")
        col.prop(settings, "radius")

        col.separator()
        
        col.label(text="Viewport Options")
        col.prop_menu_enum(settings, "gizmo_position")
        col.operator("view3d.tools_region_flip", text="Flip Tools")
        if len(space.region_quadviews) > 0:
            col.operator("screen.region_quadview", text="Disable Quadview")
        else:
            col.operator("screen.region_quadview", text="Enable Quadview")
            col.prop(space, "lock_cursor", text="Lock to Cursor")
            col.prop(view.region_3d, "lock_rotation", text="Lock Rotation")

        col.separator()

        col.label(text="Floating Menu Settings")
        col.prop(settings, "active_menu", text="")
        box = col.box()
        mList = settings.getMenuSettings(settings.active_menu)
        for i in range(7):
            box.prop(mList, "menu_slot_"+str(i+1), text="")
        context.area.tag_redraw()


class PIE_MT_Floating_Menu(Menu):
    """ Open a custom menu """
    bl_idname = "PIE_MT_Floating_Menu"
    bl_label = "Floating Menu"
    bl_description = "Customized Floating Menu"

    def draw(self, context:Context):
        settings = context.preferences.addons['touchview'].preferences
        menu = settings.getMenuSettings(context.mode)

        layout = self.layout
        pie = layout.menu_pie()
        for i in range(8):
            op = getattr(menu, "menu_slot_"+str(i+1))
            if op == "":
                continue
            elif "_MT_" in op:
                pie.menu(op)
                continue
            elif self.__operator_exists(op):
                pie.operator(op) 

    def __operator_exists(self, idname):
        try:
            names = idname.split(".")
            a = bpy.ops
            for prop in names:
                a = getattr(a, prop)
            a.__repr__()
        except:
            return False
        return True
