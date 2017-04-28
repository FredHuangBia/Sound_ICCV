import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob

cmd = []
print sys.argv
beg = int(sys.argv[1])
end = int(sys.argv[2])
thnum = int(sys.argv[3])
overwrite = int(sys.argv[4])
host = os.uname()[1]

for x in range(beg,end+1):
    for mat in range(0,8):
        cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Pre_Calc_EV.py %d %d %d %s'%(x,mat,overwrite,host))

pool = Pool(thnum)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt
