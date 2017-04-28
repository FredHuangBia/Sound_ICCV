import os
import sys
import subprocess
import json
from sound_utils import *

entries = GetEntryV1()
f = open(os.path.join(ROOT,'stat','audio_length.txt'),'w')
for entry in entries:
	print entry.path
	for audio in entry.objs:
		f.write(entry.audio[obj])
		f.write(': ')
		t=GetVidLength(entry.audio[obj]);
		f.write(t[0][18:23])
		f,write('\n')