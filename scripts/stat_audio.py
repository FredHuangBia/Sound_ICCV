import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob
import math
density = [2700,1050,7850,615,750,8200,1200,2700]
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


args = []
for k in task_list.keys():

    for v in task_list[k]:
        flag = 0
        sceneid = 1000
        obj_id = k
        mat_id = v
        target_dir = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/moments/moments.pbuf'\
            %(obj_id,mat_id)

            #print target_dir
        if not os.path.exists(target_dir):
            continue
        result_dir = os.path.join('/data/vision/billf/object-properties/sound/sound/result/','scene-%d/obj-101-%d/mat-4-%d'%(sceneid,obj_id,mat_id))
        if os.path.exists(os.path.join(result_dir,'obj-%04d.wav'%obj_id)):
            args.append([k,v])
            print k,v
print len(args)
path = '/data/vision/billf/object-properties/sound/www/audio_stat.html'
html = open(path,'w+')
col_num = 5
html.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Video Results</title>\n')
html.write('</head>\n<body>\n<table border="1">')
cnt = 0

while cnt<len(args):
	print cnt
	html.write('<tr>\n')
	for col in range(col_num):
		if cnt>=len(args):
			break
		objid = args[cnt][0]
		matid = args[cnt][1]
		volume = float(open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/volume.txt'%objid).readlines()[0])
		src = 'http://friday.csail.mit.edu/sound/result_render/scene-1000/obj-101-%d/mat-4-%d/obj-%04d.wav'%(objid,matid,objid)
		html.write('<td>\n')
		html.write('<audio controls><source src="%s" type="audio/wav"></audio>'%src)
		html.write('<br> obj=%d   mat=%d'%(objid,matid))
		html.write('<br> mass = %d density = %d'%(volume*float(density[matid]),density[matid]))
		html.write('</td>\n')
		cnt+=1
	html.write('</tr>\n')
html.write('</body>\n</html>\n')
html.close()

