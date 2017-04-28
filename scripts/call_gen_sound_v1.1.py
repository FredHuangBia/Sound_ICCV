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
'''
entries = GetEntry()
print len(entries)
render_cmd = []
'''
render_cmd=[]
#cont_entry = open('/data/vision/billf/object-properties/sound/ztzhang/continue_entry.txt')
cont_entry = open('/data/vision/billf/object-properties/sound/sound/stat/Repeat.txt')
entries=[]
for line in cont_entry.readlines():
	if line[0] =='\n' or line[0] =='-':
		continue
	else:
		entries.append(Entry(line.strip('\n')))

for entry in entries:
	render_cmd.append(entry.entry)
print len(render_cmd)


#Call all machines

cpumachines = []#[1,2]
gpumachines = [3,4,5,6,7,8,9,10,11,12,13,14]
num_m = len(cpumachines)+len(gpumachines)

cmd_args = PartitionCmd(render_cmd,num_m)
#print cmd_args


optlist, args = getopt.getopt(sys.argv[1:], 't')
mid = int(args[0])
istest = False

for k,v in optlist:
	if k == '-t':
		istest = True


cmd = []
testfile = open('sound_entry_%d_repeat.txt'%mid,'w')
for x in cmd_args[mid]:
	cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_v1.1.py -r -v -c %s'%x)
	testfile.write(x)
	testfile.write('\n')
print len(cmd)
testfile.close()





#for c in cmd:
#	print c
if not istest:
	pool = Pool(10)
	failedCmdCnt = 0
	for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
	    if returnCode != 0:
	        failedCmdCnt += 1
	print 'failed cmd: ', failedCmdCnt




		