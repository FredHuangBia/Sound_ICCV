# orig
import bpy
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(3.642959, -4.03711, 5.48463), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(0, -6, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-3.642959, 3.53711, 3.08463), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

for s in range(41):
    obj_list_path = "/data/vision/billf/object-properties/sound/sound/exp/objects/random_selected_objects/split-"+str(s)+"/selected_list_"+str(s)+".txt"
    obj_list = open(obj_list_path, "r")
    num_split = sum(1 for line in obj_list)
    obj_list.close()
    folder = "/data/vision/billf/object-properties/sound/sound/exp/objects/random_selected_objects/split-"+str(s)+"/" + str(s) + "-"
    for i in range(num_split):
        obj_path = folder  + str(i)+".orig.obj"
        obj_name = str(i)+".orig"
        try:
            bpy.ops.import_scene.obj(filepath = obj_path)
        except:
            continue
        bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        camera = bpy.data.objects["Camera"]
        obj = bpy.data.objects[0]
        max_dim=max(obj.dimensions)
        dim_y=obj.dimensions[1]
        dim_z=obj.dimensions[2]
        bpy.context.scene.objects.active = camera
        camera.constraints.new('TRACK_TO')
        camera.constraints['Track To'].target=obj
        camera.constraints['Track To'].track_axis= 'TRACK_NEGATIVE_Z'
        camera.constraints['Track To'].up_axis= 'UP_Y'
        bpy.ops.transform.translate(value=(0, 0, 1.8*max_dim), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
        bpy.ops.transform.translate(value=(-1.8*max_dim, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
        bpy.ops.transform.translate(value=(0, 1.8*max_dim, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
        bpy.context.scene.render.filepath="/data/vision/billf/object-properties/sound/www_random/imgs/split-"+str(s)+"/orig/"+str(i)+"_0.png"
        bpy.context.scene.camera = camera
        bpy.ops.render.render(write_still=True)
        bpy.ops.object.delete()
        bpy.context.scene.objects.active = obj
        obj.select=True
        bpy.ops.object.delete()

    print('\033[93mFineshed parsing: split-' +  str(s) +'\033[0m')

print('Fineshed All')
