import os

bpy.context.scene.render.engine = 'CYCLES'
bpy.ops.object.select_all(action='SELECT')
objid = 65
bpy.context.selected_objects[0].name = 'mesh%d'%objid
current_obj = bpy.data.objects['mesh%d'%objid]

for x in range(len(current_obj.material_slots)):
    mat = current_obj.material_slots[x]
    if mat.name[0:7]=='texture':
        filename =""
        ext = ""
        name = mat.name.split("-")
        filename = name[1]
        ext = name[2][0:3]
        matdata = bpy.data.materials[mat.name]
        matdata.name = '%d-%s'%(objid,mat.name)
        matdata.use_nodes = True
        nt = matdata.node_tree
        nodes = nt.nodes
        links = nt.links
        diffuse = nodes['Diffuse BSDF']
        texture = nodes.new('ShaderNodeTexImage')
        imgpath = os.path.join('/Users/zhengjia/Desktop/final100','%d'%objid,'images','%s.%s'%(filename,ext))
        texture.image = bpy.data.images.load(imgpath)
        links.new(diffuse.inputs['Color'],texture.outputs['Color'])
