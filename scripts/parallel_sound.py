import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob

cmd=[]
obj_calc = []
mat_calc = []
for obj in range(1,100):
    for mat in range(0,7):
        if os.path.exists('/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/bem_result/output-59.dat'%(obj,mat)):
            obj_calc.append(obj)
            mat_calc.append(mat)

            print obj
            
            
# Scene 1000

print obj_calc
print mat_calc
for x in range(0,len(obj_calc)):
    cmd.append('python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_New.py -r 1000 101 0 %d %d'%(obj_calc[x],mat_calc[x]))
    
    

pool = Pool(30)
failedCmdCnt = 0
for i, returnCode in enumerate(pool.imap(partial(call, shell = True), cmd)):
    if returnCode != 0:
        failedCmdCnt += 1
print 'failed cmd: ', failedCmdCnt
