import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob

beg_line = int(sys.argv[1])
end_line = int(sys.argv[2])
thnum = int(sys.argv[3])
filtered_cmd = open('/data/vision/billf/object-properties/sound/sound/script/sound_gen_entry.txt','r');
cmd_lines = []
for line in filtered_cmd.readlines():
	cmd_lines.append(line.strip('\n'))
cmd_args = []
for x in range(beg_line,end_line):
	if x>=len(cmd_lines):
		break
	else:
		cmd_args.append(cmd_lines[x])
cmd = []
for x in cmd_args:
	cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_New.py -r -v %s'%x)
for c in cmd:
	print c


pool = Pool(thnum)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt
