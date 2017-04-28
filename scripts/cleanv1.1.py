import os
import sys
import subprocess
import json
ROOT = '/data/vision/billf/object-properties/sound/sound/'
scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.1.txt')).readlines()
cnt = 0
for entry in scene_entry:
	sceneid = int(entry.split()[0])
	args = entry.split()[1:]
	objs = []
	mats = []
	for x in range(len(args)/2):
		obj_id = int(args[x*2])
		mat_id = int(args[x*2+1])
		objs.append(obj_id)
		mats.append(mat_id)
	objdir = "obj"
	matdir = "mat"
	for objid in range(len(objs)):
		objdir+="-%d"%(objs[objid])
	for matid in range(len(mats)):
		matdir+='-%d'%(mats[matid])
	resultdir = os.path.join(ROOT,'result/scene-%d'%sceneid,objdir,matdir)
	if os.path.exists(resultdir):
		print resultdir
		cnt+=1
		subprocess.call('rm -rf %s'%resultdir,shell=True)
print cnt