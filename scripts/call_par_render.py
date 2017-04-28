import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob
import math
from sound_utils import*
import getopt

####
optlist, args = getopt.getopt(sys.argv[1:], 't')

istest = False
for k,v in optlist:
	if k == '-t':
		istest = True


#entries = GetEntry()
#print len(entries)
f = open(os.path.join(ROOT,'stat','video_not_ready.txt'))
entries = []
for line in f.readlines():
	entries.append(Entry(line))
print len(entries)



####
render_cmd = []
for entry in entries:
	render_cmd.append(entry.entry)
print len(render_cmd)


#####
cpumachines = [6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,28]#31,32,33,34,35,36,37,38]
gpumachines = []#[3,5,7,10,12,13,14]#[2,3,4,6,7,8,10,11,12,14,15,20]#[2,3,5,7,8,10,11,12,13,14,20]
num_m = len(cpumachines)+len(gpumachines)

####
cmd_args = PartitionCmd(render_cmd,num_m)
print len(cpumachines)


cmd = []
####
for cnt in range(len(cpumachines)):
	filtered_cmd = open('render_entry_all_continue_%d.txt'%cnt,'w');
	for x in cmd_args[cnt]:
		filtered_cmd.write('%s'%x)
	filtered_cmd.close()
	cmd.append('ssh -f vision%02d python /data/vision/billf/object-properties/sound/sound/script/call_render_all.py 1 %d >%d.txt'%(cpumachines[cnt],cnt,cpumachines[cnt]))



#######
cm = len(cpumachines)
for cnt in range(len(gpumachines)):
	filtered_cmd = open('render_entry_all_continue_%d.txt'%(cnt+cm),'w');
	for x in cmd_args[cnt+cm]:
		filtered_cmd.write('%s'%x)
	filtered_cmd.close()
	cmd.append('ssh -f visiongpu%02d python /data/vision/billf/object-properties/sound/sound/script/call_render_all.py 1 %d >gpu%d.txt'%(gpumachines[cnt],cnt+cm,gpumachines[cnt]))


if not istest:
	for x in range(len(cmd)):
		print cmd[x]
		call(cmd[x],shell = True)
else:
	for s in cmd:
		print s

		
