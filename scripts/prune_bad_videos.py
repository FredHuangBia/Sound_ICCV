import sys,getopt,ConfigParser,os
import json
import subprocess
import math
from sound_utils_v1_1 import *
entries = []
f = open(os.path.join(ROOT,'stat','video_bad.txt'),'r')
for line in f.readlines():
    entries.append(Entry(line))

print len(entries)

for entry in entries:
	print 'mv %s %s'%(entry.video,os.path.join(entry.path,'sli_bad.mp4'))
	subprocess.call('mv %s %s'%(entry.video,os.path.join(entry.path,'sli_bad.mp4')),shell=True)