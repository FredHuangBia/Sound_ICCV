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
            if data[k]=='1' and k<=8 and k!=6:
                target_dir = '/data/vision/billf/object-properties/sound/sound/result/scene-1000/obj-101-%d/mat-4-%d/obj-%04d.wav'\
			%(obj_id,k-1,obj_id)
                if os.path.exists(target_dir):
                    task_list[obj_id].append(k-1)
                    cnt+=1
print cnt


scene_entry = '/data/vision/billf/object-properties/sound/sound/config/scene/stat.txt'
scene_args = open(scene_entry,'r')
render_cmd = []
audio_ready = []
video_ready = []
ready = []
for line in scene_args.readlines():
	#print line
	sceneid = int(line.split()[0])
	args = line.split()[1:]
	#print args
	flag = 0
	objs = []
	mats = []
	for x in range(len(args)/2):

		obj_id = int(args[x*2])
		mat_id = int(args[x*2+1])

		objs.append(obj_id)
		mats.append(mat_id)
		if obj_id<=100:
			target_dir = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/moments/moments.pbuf'\
			%(obj_id,mat_id)
			#print target_dir
			if not os.path.exists(target_dir) or mat_id==5:
				flag = 1
			if mat_id==5:
				flag==1
				#print "5!!!!"
			if not obj_id in task_list.keys():
				flag = 1
				#print "obj!!!!!"
			elif not mat_id in task_list[obj_id]:
				flag = 1
				#print "mat!!!!!!"
				#print obj_id,mat_id
	if flag==0:
		render_cmd.append(line)
		objdir = "obj"
		matdir = "mat"
		for objid in range(len(objs)):
			objdir+="-%d"%(objs[objid])
		for matid in range(len(mats)):
			matdir+='-%d'%(mats[matid])
		resultdir = os.path.join('/data/vision/billf/object-properties/sound/sound/result/scene-%d'%sceneid,objdir,matdir)
		#print resultdir
		wav_flag = 0
		for obj in objs:
			if obj>=100:
				continue
			if not os.path.exists(os.path.join(resultdir,'obj-%04d.wav'%obj)):
				wav_flag=1
		if wav_flag==0:
			audio_ready.append(line)
		if os.path.exists(os.path.join(resultdir,'sli.mp4')):
			video_ready.append(line)
			if wav_flag==0:
				ready.append(line)

with open('/data/vision/billf/object-properties/sound/sound/stat/audio_ready.txt','w') as f:
	f.writelines(audio_ready)
with open('/data/vision/billf/object-properties/sound/sound/stat/video_ready.txt','w') as f:
	f.writelines(video_ready)
with open('/data/vision/billf/object-properties/sound/sound/stat/all_ready.txt','w') as f:
	f.writelines(ready)
print len(audio_ready)
print len(video_ready)
print len(ready)




