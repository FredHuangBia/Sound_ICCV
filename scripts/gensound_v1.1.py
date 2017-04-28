import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob
import math
ROOT = '/data/vision/billf/object-properties/sound/sound/'
scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.1.txt')).readlines()
cnt = 0
render_cmd = []
for entry in scene_entry:
		render_cmd.append(entry)

print len(render_cmd)


cmd = []
cpumachines = range(10)
gpumachines = []
num_m = len(cpumachines)+len(gpumachines)
partition = range(0,len(render_cmd)+30,int(math.ceil((len(render_cmd)+13)/(num_m))))

hid = int(sys.argv[1])


beg_line = partition[hid]
end_line = partition[hid+1]
print beg_line,end_line
cmd_args=[]
for x in range(beg_line,end_line):
	if x>=len(render_cmd):
		break
	else:
		cmd_args.append(render_cmd[x])
cmd = []
for x in cmd_args:
	cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_New.py -r -v -c %s'%x)

pool = Pool(10)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt



		