import os
import sys
import subprocess
import json

cpumachines = [3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,28,29,31,32,33,34,35,36,37,38]
gpumachines = [3,5,6,7,10,11,12,13,14]#[2,3,4,6,7,8,10,11,12,14,15,20]#[2,3,5,7,8,10,11,12,13,14,20]

cmd = []
for m in cpumachines:
	cmd.append('ssh -f vision%02d \'echo -test \''%m)

for m in gpumachines:
    cmd.append('ssh -t visiongpu%02d \'echo -test\' '%(m))
        


print 'HA!'
for c in cmd:
	print c
	subprocess.call(c,shell=True)