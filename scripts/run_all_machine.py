import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
import subprocess
import glob
machine = [1,2,3,4,5,6,8,9,11,13,14,15,16,17,18,19,21,22,23,24,25,26,27,29,30,31,32,33,37,38]
threnum = [6,6,6,6,6,6,6,6, 6, 6, 6,15, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
gpumachine = [ 3, 4, 6, 7, 9,12,16,20]
gputhrenum = [15,15,15,15,15,15,15,15]
for x in range(0,len(machine)):
    beg = x*2
    end = beg+1
    
    cmd = 'ssh -f vision%02d \'nohup bash /data/vision/billf/object-properties/sound/sound/script/calcEV.sh %d %d %d 0\'>vision%02d.txt'\
    %(machine[x],beg,end,threnum[x],machine[x])
    print cmd
    subprocess.call(cmd,shell=True)
    os.system('read -s -n 1 -p "Press any key to continue..."')
    print
for x in range(0,len(gpumachine)):
    beg_gpu = end+1+x*5
    end_gpu = beg_gpu+4
    cmd = 'ssh -f visiongpu%02d \'nohup bash /data/vision/billf/object-properties/sound/sound/script/calcEV.sh %d %d %d 0\'>visiongpu%02d.txt'\
    %(gpumachine[x],beg_gpu,end_gpu,gputhrenum[x],gpumachine[x])
    print cmd
    subprocess.call(cmd,shell=True)
    os.system('read -s -n 1 -p "Press any key to continue..."')
    print
