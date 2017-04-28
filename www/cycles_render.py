

# orig
import os
import bpy
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
folder = "/data/vision/billf/object-properties/sound/sound/exp/objects/final100/"
good = [1,7,9,10,11,13,15,16,17,19,20,26,32,38,40,42,44,45,47,49,50,52,53,55,56,58,60,64,65,68,73,78,81,84,85,87,92,94,99]
for i in good:
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2.2, 2.2, 2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(0, 0, 3.3), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2.2, 2.2, -2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2.2, -2.2, 2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2.2, -2.2, -2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
 #   bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2, 2, 2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
 #   bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2, 2, 2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
 #   bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2, 2, 2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-2.2, 2.2, 2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-2.2, 2.2, -2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
 #   bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-2, 2, 2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
 #   bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-2, 2, 2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-2.2, -2.2, 2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(-2.2, -2.2, -2.2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2, -2, 1), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#    bpy.ops.object.lamp_add(type='POINT', radius=1, view_align=False, location=(2, -2, 1), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    objid = i
    obj_path = folder  + str(i) + "/models/" + str(i) + ".orig.obj"
    bpy.ops.import_scene.obj(filepath = obj_path)
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
    bpy.ops.transform.translate(value=(0, 0, 1.36*max_dim), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    bpy.ops.transform.translate(value=(1.36*max_dim, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    bpy.ops.transform.translate(value=(0, -2*max_dim, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
    bpy.context.scene.render.filepath="/data/vision/billf/object-properties/sound/www_random/imgs/orig/"+str(i)+"_1.png"
    bpy.context.scene.camera = camera
    
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.ops.object.select_all(action='SELECT')
    bpy.context.selected_objects[0].name = 'mesh%d'%objid
    current_obj = bpy.data.objects['mesh%d'%objid]

    for x in range(len(current_obj.material_slots)):
        mat = current_obj.material_slots[x]
        if mat.name[0:7]=='texture':
            filename =""
            ext = ""
            cnt = 0
            for x in range(8,len(mat.name)):
                if cnt == 0 and mat.name[x]!='-':
                    filename+=mat.name[x]
                elif cnt == 0 and mat.name[x]=='-':
                    cnt = 1
                elif cnt == 1:
                    ext+=mat.name[x]
            matdata = bpy.data.materials[mat.name]
            matdata.name = '%d-%s'%(objid,mat.name)
            matdata.use_nodes = True
            nt = matdata.node_tree
            nodes = nt.nodes
            links = nt.links
            diffuse = nodes['Diffuse BSDF']
            texture = nodes.new('ShaderNodeTexImage')
            imgpath = os.path.join('/data/vision/billf/object-properties/sound/sound/exp/objects/final100','%d'%objid,'images','%s.%s'%(filename,ext))
            texture.image = bpy.data.images.load(imgpath)
            links.new(diffuse.inputs['Color'],texture.outputs['Color'])

    #bpy.ops.import_scene.obj(filepath = "/data/vision/billf/object-properties/sound/qiujiali/ground.obj")
    bpy.context.scene.world.horizon_color = (1.0, 1.0, 1.0)
    bpy.ops.render.render(write_still=True)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.context.scene.objects.active = obj
    obj.select=True
    bpy.ops.object.delete()
print('Fineshed')



import os
import bpy
objid = 9
bpy.context.scene.render.engine = 'CYCLES'
bpy.ops.object.select_all(action='SELECT')
bpy.context.selected_objects[0].name = 'mesh%d'%objid
current_obj = bpy.data.objects['mesh%d'%objid]

for x in range(len(current_obj.material_slots)):
    mat = current_obj.material_slots[x]
    if mat.name[0:7]=='texture':
        filename =""
        ext = ""
        cnt = 0
        for x in range(8,len(mat.name)):
            if cnt == 0 and mat.name[x]!='-':
                filename+=mat.name[x]
            elif cnt == 0 and mat.name[x]=='-':
                cnt = 1
            elif cnt == 1:
                ext+=mat.name[x]
        matdata = bpy.data.materials[mat.name]
        matdata.name = '%d-%s'%(objid,mat.name)
        matdata.use_nodes = True
        nt = matdata.node_tree
        nodes = nt.nodes
        links = nt.links
        diffuse = nodes['Diffuse BSDF']
        texture = nodes.new('ShaderNodeTexImage')
        imgpath = os.path.join('/Users/zhengjia/Desktop/sound/sound/exp/objects/final100','%d'%objid,'images','%s.%s'%(filename,ext))
        texture.image = bpy.data.images.load(imgpath)
        links.new(diffuse.inputs['Color'],texture.outputs['Color'])


