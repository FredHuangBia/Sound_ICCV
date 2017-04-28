import os
import sys
import subprocess
import json
ROOT = '/data/vision/billf/object-properties/sound/sound/'
scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.1.txt')).readlines()
cnt = 0
audio_ready = []
video_ready = []
ready = []
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
#		print 'yes!'
		wav_flag = 0
		vid_flag = 0
		for obj in objs:
			if obj>=100:
				continue
			if not os.path.exists(os.path.join(resultdir,'obj-%04d.wav'%obj)):
				wav_flag = 1
		if not os.path.exists(os.path.join(resultdir,'sli.mp4')):
			vid_flag = 1
		if wav_flag == 0:
			audio_ready.append(entry)
		if vid_flag == 0:
			video_ready.append(entry)
		if (wav_flag + vid_flag)==0:
			ready.append(entry)
print len(audio_ready)
print len(video_ready)
print len(ready)

