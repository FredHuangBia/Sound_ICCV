import sys,getopt,ConfigParser,os
import json
import subprocess
import math
import numpy as np

cnt = 300
ym_list= [15]
p_list = np.linspace(0.1,0.3,100)
for ym in ym_list:
	for p in p_list:
			mtl_cfg = ConfigParser.ConfigParser()
			#mtl_cfg.add_section('DEFAULT')
			mtl_cfg.set('DEFAULT','name','oak_%d'%cnt)
			mtl_cfg.set('DEFAULT','youngs','%E'%(ym*1000000000))
			mtl_cfg.set('DEFAULT','poison','%0.5f'%p)
			mtl_cfg.set('DEFAULT','density','%d'%2000)
			mtl_cfg.set('DEFAULT','alpha','%E'%2E-6)
			mtl_cfg.set('DEFAULT','beta','%d'%60)
			mtl_cfg.set('DEFAULT','friction','%d'%1)
			mtl_cfg.set('DEFAULT','rollingFriction','%d'%1)
			mtl_cfg.set('DEFAULT','spinningFriction','%d'%1)
			mtl_cfg.set('DEFAULT','restitution','%d'%1)
			with open(os.path.join('/data/vision/billf/object-properties/sound/sound/validation/materials','material-%d.cfg'%cnt), 'w+') as configfile:
				mtl_cfg.write(configfile)
			cnt=cnt+1


