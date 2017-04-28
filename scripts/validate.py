import scipy.io as sio
import os


obj_list_path= '/data/vision/billf/object-properties/sound/sound/data/final100/small_stats.txt'
mat_matrix_path  = '/data/vision/billf/object-properties/sound/sound/data/material_matrix.dat'
obj_list_file = open(obj_list_path,'r')
mat_matrix_file = open(mat_matrix_path,'r')
task_list = dict()
for line in obj_list_file.readlines():
    obj_id = int(line.split()[0])
    task_list[obj_id] = []
for line in mat_matrix_file.readlines():
    data = line.split()
    obj_id = int(data[0])
    if not obj_id in task_list:
        continue
    else:
        for k in range(1,len(data)):
            if data[k]=='1' and k<=8:
                task_list[obj_id].append(k-1)

for k in task_list.keys():
	print k
	for v in task_list[k]:
		mesh = sio.loadmat('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_input/mesh.mat'%(k,v))
		bem_init =sio.loadmat('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_input/init_bem.mat'%(k,v))
		facenum= mesh['mesh']['face'][0][0].shape[0]
		init_num= bem_init['init_bem'].shape[1]
		if init_num!=facenum:
			print "%d mat-%d BAD!!!!!!!"%(k,v)
    
