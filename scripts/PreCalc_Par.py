import os
import sys
import subprocess
import json

#machine = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
isbem = int(sys.argv[1])
print isbem
machine = range(2,39)
thnum = 3
gpumachine = [8,13,14,20,2,3,4,5,6,7,9,10,11,12]
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


cnt = 0
args = []
cnt_a = 0
for k in task_list.keys():
    for v in task_list[k]:
        cnt_a+=1
        if not os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/'%(k,v)):
            args.append([k,v])
        elif not os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-59.dat'%(k,v)):
            args.append([k,v])
print len(args)

cnt = 0
cmd = []
thnum = 1

for m in machine:
    if m ==27:
        continue
    tmp = ""
    for th in range(0,thnum):
    	if cnt>=len(args):
            break
        tmp+="%d %d "%(args[cnt][0],args[cnt][1])
        cnt+=1
    if tmp!="":
        if isbem==1:
            cmd.append('ssh -f vision%02d \'python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%s" 1\'>vision%02d.txt '%(m,tmp,m))
        else:
    		cmd.append('ssh -f vision%02d \'python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%s"\'>vision%02d.txt '%(m,tmp,m))
              
gputhnum = 1

for m in gpumachine:
    tmp = ""
    for th in range(0,gputhnum):
        if cnt>=len(args):
            break
        tmp+="%d %d "%(args[cnt][0],args[cnt][1])
        cnt+=1
    if tmp!="":
        if isbem==1:
            cmd.append('ssh -f visiongpu%02d \' python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%s" 1\'>visiongpu%02d.txt '%(m,tmp,m))
        else:
        	cmd.append('ssh -f visiongpu%02d \' python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%s"\'>visiongpu%02d.txt '%(m,tmp,m))
        


print 'HA!'
print cnt
#print cmd
'''
for k in args:
    print k[0],k[1]
    dirs = os.listdir('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/'%(k[0],k[1]))
    ofileid = []
    for ofile in dirs:
        if ofile[8]=='.':
            ofileid.append(int(ofile[7]))
        else:
            ofileid.append(int(ofile[7:9]))
    print max(ofileid),len(ofileid)

    #outfile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-%d.dat'%(objid,matid,fid))
    #infile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/fastbem/input-%d.dat'%(objid,matid,fid))
'''
for c in cmd:
    print c
    #subprocess.call(c,shell=True)
