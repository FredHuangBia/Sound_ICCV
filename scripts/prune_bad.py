import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob

thnum =1


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

for k in range(len(args)):
    objid = args[k][0]
    matid = args[k][1]
    print "---------------------%d:%d----------------------------"%(objid,matid)
    tmp = -1
    badid = -1
    for fid in range(0,60):
        if not os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-%d.dat'%(objid,matid,fid)):
            print 'BAD!!!!OUT!!!!!!'
            #call('python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%d %d" &'%(objid,matid),shell=True)
            break
        if not os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/fastbem/input-%d.dat'%(objid,matid,fid)):
            print "MISSING INPUTS!!!"
            #call('rm -rf /data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_input/*.mat'%(objid,matid),shell=True)
            #call('python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%d %d" &'%(objid,matid),shell=True)
            break


        outfile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-%d.dat'%(objid,matid,fid))
        infile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/fastbem/input-%d.dat'%(objid,matid,fid))
        olines = outfile.readlines()
        inlines = infile.readlines()
        infile.close()
        outfile.close()
        if len(inlines)<=20 or len(olines)<=20:
            print 'BAD input file !!!'
            #call('rm -rf /data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_input/*.mat'%(objid,matid),shell=True)
            #call('python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%d %d" &'%(objid,matid),shell=True)
            break
        if tmp ==-1:
            tmp = len(olines)
        cur = len(olines)
        if tmp !=cur:
            print 'BAD!!!'
            
            break
        tmp = cur
        if olines[0].split()[6]=='\x00':
            #outfile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-%d.dat'%(objid,matid,fid),'w')
            #tmp = olines[0].split()
            #tmp[6]='0.0'
            #tmp_line = ' '.join(tmp)
            #olines[0] = "  "+tmp_line+"\n"
            #outfile.writelines(olines)
            badid = fid
            #print "REPLACED!!!!!"
        elenum_in = int(inlines[-4].split()[0])
        elenum_out = int(olines[-1].split()[0])
        #print elenum_in
        #print elenum_out
        if elenum_out!=elenum_in:
            print 'BAD elenum!!!'
            #call('rm -rf /data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_input/*.mat'%(objid,matid),shell=True)
            #call('python /data/vision/billf/object-properties/sound/sound/script/precal_machine.py "%d %d" &'%(objid,matid),shell=True)
            break
    if badid>=0 and badid <=30:
        print 'BAD freq!!!!!'
        print badid
        #wp = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/'%(objid,matid)
        #call('bash /data/vision/billf/object-properties/sound/sound/script/test.sh -p "%s" -b %d -e 59 &'\
        #    %(wp,0),shell=True)
    elif badid>30:
        print 'TOO MANY BAD FREQ!!!!!'
    else:
        print 'GOOD!'



