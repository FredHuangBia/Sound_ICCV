
import sys
import os
from subprocess import call

#objid = [23,23,41,41,41,41,48,48,48,57,57,57,61,61,61,61,68,68,70,88,88,88,95,95,98,98,98,98,98]
#matid = [6,7,0,2,6,7,2,4,7,2,5,7,2,3,4,7,0,2,4,2,5,7,3,4,1,2,3,4,7]

for x in range(len(objid)):
	print objid[x],matid[x]
	wp = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/'%(objid[x],matid[x])
	call('bash /data/vision/billf/object-properties/sound/sound/script/test.sh -p "%s" -b %d -e 59 &'\
		%(wp,0),shell=True)





#objid=int(sys.argv[1])
#matid=int(sys.argv[2])
#wp = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/'%(objid,matid)
#call('bash /data/vision/billf/object-properties/sound/sound/script/test.sh -p "%s" -b %d -e 59 &'\
#%(wp,0),shell=True)