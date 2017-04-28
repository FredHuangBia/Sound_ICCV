import os

volume_stat = open('/data/vision/billf/object-properties/sound/sound/data/final100/volume.txt')
for line in volume_stat.readlines():
	data = line.split()
	objid = data[0]
	volumes = float(data[1])
	vfile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/volume.txt'%int(objid),'w')
	vfile.write('%1.10f\n'%volumes)
	vfile.close()
	vfile = open('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/volume.txt'%int(objid),'r')
	line = vfile.readline()
	print float(line)