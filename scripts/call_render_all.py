import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob


thnum = int(sys.argv[1])
filtered_cmd_id = int(sys.argv[2])
filtered_cmd = open('/data/vision/billf/object-properties/sound/sound/script/render_entry_all_continue_%d.txt'%(filtered_cmd_id),'r');
cmd_lines = []
for line in filtered_cmd.readlines():
	cmd_lines.append(line.strip('\n'))
cmd_args = []
for x in range(0,len(cmd_lines)):
	cmd_args.append(cmd_lines[x])
cmd = []


for x in cmd_args:
	cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_v1.1.py -s -c %s'%x)
#for c in cmd:
#	print c
print len(cmd)

pool = Pool(thnum)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt
