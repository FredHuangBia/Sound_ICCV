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
        #result_dir = os.path.join('/data/vision/billf/object-properties/sound/sound/result/','scene-%d/obj-101-%d/mat-4-%d'%(sceneid,obj_id,mat_id))
        #if not os.path.exists(os.path.join(result_dir,'obj-%04d.wav'%obj_id)):
        args.append([k,v])
cmd = []
hid = int(sys.argv[1])

num = range(hid*19,(hid+1)*19)
print num[0],num[-1]

for k in num:
    if k >=len(args):
        continue
    cmd.append('python Gen_Sound_New.py -r -v 1000 101 4 %d %d'%(args[k][0],args[k][1]))
    #print cmd[-1]
print len(cmd)
print cmd



pool = Pool(10)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt



