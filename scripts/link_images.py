import os
import sys
import subprocess
root = '/data/vision/billf/object-properties/sound/sound/data/final100/'

obj_list_path= '/data/vision/billf/object-properties/sound/sound/data/final100/small_stats.txt'
obj_list_file = open(obj_list_path,'r')
objs = []
for line in obj_list_file.readlines():
    obj_id = int(line.split()[0])
    objs.append(obj_id)

for x in objs:
	if not os.path.exists(os.path.join(root,'%d/images'%x)):
		print x
		#subprocess.call('ln -s %s %s'%(os.path.join(root,'%d/images'%x),'/data/vision/billf/object-properties/sound/sound/data/ready/%d/images'%(x)),shell=True)
