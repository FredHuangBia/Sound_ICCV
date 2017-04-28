import os
import sys
import argparse
import shutil
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
import glob
import numpy as np
import multiprocessing
    
# what are your inputs, and what operation do you want to 
# perform on each input. For example...

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

def CalScore(freq,modes,weights):
	s = 0
	for m in range(0,len(modes)):
		f = find_nearest(freq,modes[m])
		#print f
		s+=np.abs((f-modes[m]))*weights[m]*weights[m]
	return s

def CalMat(mat):
	print mat
	obj = 2
	RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/validation/%d'%obj
	eigvalue= []
	if os.path.exists(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')):
		with open(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')) as f:
			for line in f.readlines():
				eigvalue.append(float(line))
	eigvalue = np.array(eigvalue)
	cnt = 0
	score = []
	
	freqs=[]
	setup = []
	for density in np.linspace(2600,2800,50):
		for alpha in np.linspace(1e-5,1e-7,50):
			for beta in np.linspace(1,100,50):
				#print'-------------------------'
				eigmodes = eigvalue/density;
				omega = np.sqrt(eigmodes);
				c = alpha*eigmodes+beta;
				x = c/(2.0*omega);
				if (x*x).max()>=1:
					#print 'SKIP!!!!'
					continue
				omegaD = omega*(np.sqrt(1.0-x*x));
				freq = omegaD/(2*np.pi);
				s = CalScore(freq,modes,weights)
				score.append(s)
				freqs.append(freq)
				setup.append([density,alpha,beta])
	print len(score)
	return mat,score[np.array(score).argmin()],freqs[np.array(score).argmin()],setup[np.array(score).argmin()]
	#print freqs[np.array(score).argmin()]
def CalMat_Oak(mat):
	print mat
	obj = 3
	RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/validation/%d'%obj
	eigvalue= []
	if os.path.exists(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')):
		with open(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')) as f:
			for line in f.readlines():
				eigvalue.append(float(line))
	else:
		print 'WRONG!!!!!'
	eigvalue = np.array(eigvalue)
	cnt = 0
	score = []
	yms = []
	freqs=[]
	setup = []
	for ym in  np.linspace(14.9E9,16E9,50):
		r = ym/1.100000E+10
		for density in np.linspace(490,600,20):
			for alpha in np.linspace(1e-5,1e-7,20):
				for beta in np.linspace(50,200,20):
					#print'-------------------------'
					eigmodes = r*eigvalue/density;
					omega = np.sqrt(eigmodes);
					c = alpha*eigmodes+beta;
					x = c/(2.0*omega);
					if (x*x).max()>=1:
						#print 'SKIP!!!!'
						continue
					omegaD = omega*(np.sqrt(1.0-x*x));
					freq = omegaD/(2*np.pi);
					s = CalScore(freq,modes,weights)
					score.append(s)
					freqs.append(freq)
					setup.append([density,alpha,beta])
					yms.append(ym)
	print len(score)
	return mat,yms[np.array(score).argmin()],score[np.array(score).argmin()],freqs[np.array(score).argmin()],setup[np.array(score).argmin()]


def CalYM(ym):
	print ym
	mat =33
	obj = 2
	RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/validation/%d'%obj
	eigvalue= []
	if os.path.exists(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')):
		with open(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')) as f:
			for line in f.readlines():
				eigvalue.append(float(line))
	else:
		return
	eigvalue = np.array(eigvalue)
	cnt = 0
	score = []
	
	freqs=[]
	setup = []
	r = ym/(5.000000E+10)
	for density in np.linspace(2500,2800,50):
		for alpha in np.linspace(1e-5,1e-8,50):
			for beta in np.linspace(90,100,50):
				#print'-------------------------'
				eigmodes = r*eigvalue/density;
				omega = np.sqrt(eigmodes);
				c = alpha*eigmodes+beta;
				x = c/(2.0*omega);
				if (x*x).max()>=1:
					#print 'SKIP!!!!'
					continue
				omegaD = omega*(np.sqrt(1.0-x*x));
				freq = omegaD/(2*np.pi);
				s = CalScore(freq,modes,weights)
				score.append(s)
				freqs.append(freq)
				setup.append([density,alpha,beta])
	return ym,score[np.array(score).argmin()],freqs[np.array(score).argmin()],setup[np.array(score).argmin()]


####Marble
modes =  1e+4*np.array([0.0438,0.5888,0.3828,0.7807,0.5802,0.7348,0.7213,1.0055]) #[400,5362,3486,7109,9156,4188,7925,2348,10368];
weights = [ 34.4087,22.4306,13.6242,13.5052,13.3886,12.4816,11.2198,10.4712] #[34.4087,22.4306,13.6242,13.5052,10.4712,6.2696,5.8478,5.6710,4.3782]


####Oak
#weights = [45.2704,17.6147,12.0168,9.5290,8.5698,8.2747,6.5868,6.3471,5.8653,5.7620]
#modes = 1e4*np.array([0.0340,0.6770,0.7571,0.8639,0.5827,0.2179,0.9515,0.4996,1.2288,0.4219])





obj = 2
RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/validation/%d'%obj
#mat = 33
base = 0
eigvalue= []
min_s = []
freq_min = []
set_up_min = []

inputs = range(100) 
pool = multiprocessing.Pool(20)
    
mats,min_s, freq_min, set_up_min = zip(*pool.map(CalMat, range(0,100)))
#CalMat_Oak(100)
#mats,yms,min_s, freq_min, set_up_min = zip(*pool.map(CalMat_Oak, range(100,200)))

mat = mats[np.array(min_s).argmin()]
#ym = yms[np.array(min_s).argmin()]
print mat#,ym

#mats,min_s, freq_min, set_up_min = zip(*pool.map(CalYM, np.linspace(4.6E+10,5.3E10,100)))
#ym = mats[np.array(min_s).argmin()]
#mat = 33
#print ym
#mat = 0

setup = set_up_min[np.array(min_s).argmin()]
obj = 2
RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/validation/%d'%obj
eigvalue= []
if os.path.exists(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')):
	with open(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')) as f:
		for line in f.readlines():
			eigvalue.append(float(line))
eigvalue = np.array(eigvalue)

#r = ym/1.100000E+10
r=1
eigmodes = r * eigvalue/setup[0];
omega = np.sqrt(eigmodes);
c = setup[1]*eigmodes+setup[2]
x = c/(2.0*omega)
print x
omegaD = omega*(np.sqrt(1.0-x*x))
freq = omegaD/(2*np.pi)


for m in modes:
	print find_nearest(freq,m)
'''
eigmodes = eigvalue/setup[0];
omega = np.sqrt(eigmodes);
c = setup[1]*eigmodes+setup[2];
x = c/(2.0*omega);
omegaD = omega*(np.sqrt(1.0-x*x));
freq = omegaD/(2*np.pi);
print freq
'''

'''
for mat in range(100):
	print mat
	eigvalue= []
	if os.path.exists(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')):
		with open(os.path.join(RESULT_ROOT,'mat-%d'%mat,'log.txt')) as f:
			for line in f.readlines():
				eigvalue.append(float(line))
	eigvalue = np.array(eigvalue)
	cnt = 0
	score = []
	
	freqs=[]
	setup = []
	for density in np.linspace(2600,2800,50):
		for alpha in np.linspace(1e-5,1e-10,50):
			for beta in np.linspace(1,1000,50):
				#print'-------------------------'
				eigmodes = eigvalue/density;
				omega = np.sqrt(eigmodes);
				c = alpha*eigmodes+beta;
				x = c/(2.0*omega);
				if (x*x).max()>=1:
					#print 'SKIP!!!!'
					continue
				omegaD = omega*(np.sqrt(1.0-x*x));
				freq = omegaD/(2*np.pi);
				s = CalScore(freq,modes,weights)
				score.append(s)
				freqs.append(freq)
				setup.append([density,alpha,beta])
	min_s.append(score[np.array(score).argmin()])
	#print freqs[np.array(score).argmin()]
	freq_min.append(freqs[np.array(score).argmin()])
	set_up_min.append(setup[np.array(score).argmin()])
'''
print np.array(min_s).min()
print freq_min[np.array(min_s).argmin()]
print set_up_min[np.array(min_s).argmin()]
