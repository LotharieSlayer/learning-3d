	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Light']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Light']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cylinder']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cylinder']
	bpy.ops.transform.translate(value=(0.337583, 0.352919, -0.0951244), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['drawing_face']]
	bpy.context.view_layer.objects.active = bpy.data.objects['drawing_face']
	bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube.001']
	bpy.ops.transform.translate(value=(3.39938, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
	bpy.ops.transform.resize(value=(0.253869, 0.253869, 0.253869), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
	bpy.ops.object.delete(use_global=False, confirm=False)
