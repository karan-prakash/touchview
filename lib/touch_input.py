import bpy

modes = ("Object Mode", "Mesh", "Sculpt", "Vertex Paint", "Weight Paint", "Image Paint")

addon_keymaps = []
addon_tweaks = []

# added timer to ensure Blender keyconfig is fully populated before running
def register_keymaps():
    bpy.app.timers.register(assign_keymaps, first_interval=0.2)

# toggle active addon_keymaps and addon_tweaks
def toggle_keymaps(state: bool = True):
    for km, kmi in addon_keymaps:
        if kmi.type == 'LEFTMOUSE' and kmi.value != 'DOUBLE_CLICK':
            kmi.active = state
        elif kmi.type == 'MIDDLEMOUSE' and bpy.context.preferences.addons['touchview'].preferences.include_mmb:
            kmi.active = state
    for kmi, original in addon_tweaks:
        if not state:
            kmi.active = original
        else:
            kmi.active = False


# two main goals: preserve action from MOUSE to PEN, add viewport control to MOUSE
def assign_keymaps():
    wm = bpy.context.window_manager   

# add global default action
    km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type='VIEW_3D')
    kmi = km.keymap_items.new('view3d.toggle_touch', type='T', value='PRESS', alt=True)
    addon_keymaps.append((km, kmi))

    km = wm.keyconfigs.addon.keymaps.new(name="", space_type='EMPTY')
    kmi = km.keymap_items.new('view3d.dt_action', 'MIDDLEMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi)) 

    kmi = km.keymap_items.new('view3d.view_ops', 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

# add LEFT MOUSE ACTION for view3d.view_ops
    for kmap in wm.keyconfigs['Blender'].keymaps:
        # isolate modes where we can use pen and mouse for different actions
        if "Node" in kmap.name or "3D View" in kmap.name or kmap.name in modes:
            flipped = False
            commands = []
            for item in kmap.keymap_items:
                if item.map_type in ("MOUSE","TWEAK") and item.type in ("LEFTMOUSE", "EVT_TWEAK_L") and not any((item.oskey, item.ctrl, item.alt, item.shift)):
                    if("Node" in kmap.name):
                        if(item.map_type == "TWEAK"):
                            continue
                    flipped = True
                    addon_tweaks.append((item, item.active))
                    item.active = False
                    commands.append(item.idname)

            # if we flipped a mouse to pen action, add mouse control
            if flipped or kmap.name in modes:
                main_action = "view2d.view_ops" if "Node" in kmap.name else "view3d.view_ops"
                km = wm.keyconfigs.addon.keymaps.new(name=kmap.name, space_type=kmap.space_type)
                kmi = km.keymap_items.new(main_action, 'MIDDLEMOUSE', 'PRESS')
                addon_keymaps.append((km, kmi)) 

                kmi = km.keymap_items.new(main_action, 'LEFTMOUSE', 'PRESS')
                addon_keymaps.append((km, kmi))
                
                kmi = km.keymap_items.new('view3d.dt_action', 'LEFTMOUSE', 'DOUBLE_CLICK')
                addon_keymaps.append((km, kmi)) 
                
                # reassign default action to PEN
                if len(commands) != 0:
                    for command in commands:
                        kmi = km.keymap_items.new(command, 'PEN', 'PRESS')
                        addon_keymaps.append((km, kmi)) 

    # make menus draggable
    km = wm.keyconfigs.addon.keymaps.new(name='View2D Buttons List', space_type='EMPTY')
    kmi = km.keymap_items.new('view2d.pan', 'LEFTMOUSE', 'PRESS')
    addon_keymaps.append((km, kmi))

# unset MOUSE viewport control, reset PEN to MOUSE input
def unregister_keymaps():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    for kmi, state in addon_tweaks:
        kmi.active = state
    addon_keymaps.clear()
    addon_tweaks.clear()
