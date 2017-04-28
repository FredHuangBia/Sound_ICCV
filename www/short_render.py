#track_camera

# for  RaLb
import bpy
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(3.642959, -4.03711, 5.48463), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(0, 6, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-3.642959, 3.53711, 3.08463), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))



for r in range(6,8,1):
    short_file = open("shortlist.txt")
    for l in range(3,4,1):
        folder = "../sound/exp/objects/random_selected_objects/R" + str(r) + "L" + str(l) +"/"
        for line in short_file.readlines():
            if line.split()[0] == '#' or len(line.split())==0:
                continue
            i = int(line.split()[0])
            obj_path = folder + "obj-" + str(i) + ".obj"
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
            bpy.context.scene.render.filepath="imgs/"+ "R" + str(r) + "L" + str(l) +"/" + str(i) + "_R" + str(r) + "L" + str(l) + ".png"
            bpy.context.scene.camera = camera
            bpy.ops.render.render(write_still=True)
            bpy.ops.object.delete()
            bpy.context.scene.objects.active = obj
            obj.select=True
            bpy.ops.object.delete()
    short_file.close()
print('Fineshed')



