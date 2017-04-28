import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
import subprocess
import glob

machine = [1,2,4,6,7,11,13,14,15,17,19,21,23,24,25,27,29,30,31,32,33,37,38]
thnum = 3
gpumachine = [11,12,13,14,15,20]
job = 0
overwrite = 1;
for obj in [1,11,13]:
    for mat in range(0,8):
        machine_id = int(job/thnum)
        host = machine[machine_id]
        path = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d'%(obj,mat)
        cmd = 'ssh -f vision%02d \'nohup bash /data/vision/billf/object-properties/sound/sound/script/CalcFMM.sh %s %d\' > vision%2d.txt'\
                %(host,path,overwrite,host)
        print cmd
        subprocess.call(cmd,shell=True)
        job+=1

for obj in [15,16,17,32,51,55,81,92,52,42,44]:
    for mat in range(0,4):
        machine_id = int(job/thnum)
        host = machine[machine_id]
        path = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d'%(obj,mat)
        cmd = 'ssh -f vision%02d \'nohup bash /data/vision/billf/object-properties/sound/sound/script/CalcFMM.sh %s %d\' > vision%2d.txt'\
                %(host,path,overwrite,host)
        print cmd
        subprocess.call(cmd,shell=True)
        job+=1