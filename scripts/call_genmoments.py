import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob

thnum =20


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
                
args=[]

for k in task_list.keys():
    for v in task_list[k]:
        if os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-59.dat'%(k,v)):
            if not os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/moments/moments.pbuf'%(k,v)):
        		args.append([k,v])
print len(args)

cmd = []
for k in args:
	path = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/'%(k[0],k[1])
	cmd.append('bash /data/vision/billf/object-properties/sound/sound/script/call_genmoments.sh "%s"'%(path))
print len(cmd)




pool = Pool(thnum)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt
