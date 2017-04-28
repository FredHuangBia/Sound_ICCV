import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob

objid = int(sys.argv[1])
beg = int(sys.argv[2])
end = int(sys.argv[3])
thnum = int(sys.argv[4])
cmd=[]
for x in range(beg,end+1):
    cmd.append('python /data/vision/billf/object-properties/sound/sound/script/validate_precal.py %d %d %d %s'%(objid,x,1,'gpu20'))


pool = Pool(thnum)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt
