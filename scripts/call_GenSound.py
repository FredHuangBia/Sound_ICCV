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

entries = GetEntryV1()
print len(entries)
render_cmd = []

for entry in entries:
	render_cmd.append(entry.entry)
print len(render_cmd)


#Call all machines

cpumachines = []
gpumachines = [2,3,5,6,7,8,9,10,11,12,13,14]
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
for x in cmd_args[mid]:
	cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_New.py -r -v -c %s'%x)
print len(cmd)

#for c in cmd:
#	print c
if not istest:
	pool = Pool(10)
	failedCmdCnt = 0
	for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
	    if returnCode != 0:
	        failedCmdCnt += 1
	print 'failed cmd: ', failedCmdCnt




		