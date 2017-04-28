import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob
import math

obj_list_path= '/data/vision/billf/object-properties/sound/sound/data/final100/small_stats.txt'
mat_matrix_path  = '/data/vision/billf/object-properties/sound/sound/data/material_matrix.dat'
obj_list_file = open(obj_list_path,'r')
mat_matrix_file = open(mat_matrix_path,'r')
task_list = dict()
cnt = 0
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
                cnt+=1
print cnt

cnt = 0
for k in task_list.keys():
	for v in task_list[k]:
		target_dir = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/moments/moments.pbuf'\
			%(k,v)
		if not os.path.exists(target_dir):
			print k,v
			cnt+=1
print cnt


scene_entry = '/data/vision/billf/object-properties/sound/sound/config/scene/stat.txt'
scene_args = open(scene_entry,'r')
render_cmd = [];
for line in scene_args.readlines():
	#print line
	sceneid = int(line.split()[0])
	args = line.split()[1:]
	#print args
	flag = 0
	matargs = []
	objargs=[]
	for x in range(len(args)/2):
		obj_id = int(args[x*2])
		mat_id = int(args[x*2+1])
		objargs.append(obj_id)
		matargs.append(mat_id)
		
		if obj_id<=100:
			target_dir = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/moments/moments.pbuf'\
			%(obj_id,mat_id)

			#print target_dir
			if not os.path.exists(target_dir):
				flag = 1
				#print obj_id,mat_id
	if flag==0:
		valid = 1
		obj_dir = "obj"
		mat_dir = "mat"
		for objid in objargs:
			obj_dir+="-%d"%(objid)
		for matid in matargs:
			mat_dir+="-%d"%(matid)
		result_dir = os.path.join('/data/vision/billf/object-properties/sound/sound/result/','scene-%d'%sceneid,obj_dir,mat_dir)
		for objid in objargs:
			if objid>=100:
				continue
			if not os.path.exists(os.path.join(result_dir,'obj-%04d.wav'%objid)):
				valid = 0
		if valid==1:
			render_cmd.append(line)

print len(render_cmd)
#filtered_cmd = open('sound_gen_entry.txt','w');
#for x in render_cmd:
#	print x
	#filtered_cmd.write('%s'%x)
#filtered_cmd.close()


