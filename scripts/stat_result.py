import os
import sys
from  sound_utils import *


entries = GetEntryV1()


video_list = []
for entry in entries:
    video_list.append(entry.video)

path = '/data/vision/billf/object-properties/sound/www/video_stat.html'
html = open(path,'w+')
col_num = 4
html.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Video Results</title>\n')
html.write('</head>\n<body>\n<table border="1">')
cnt = 0
while cnt<len(video_list):
    html.write('<tr>\n')
    for col in range(col_num):
        if cnt>=len(video_list):
            break
        html.write('<td>\n')
        html.write('<video width="320" height="240" controls>\n<source src="%s" type="video/mp4">\n</video>'%video_list[cnt])
        html.write('<br> scene:%d obj: %s mat %s'%(entries[cnt].scene,entries[cnt].ObjsToString(),entries[cnt].MatsToString()))
        html.write('</td>\n')
        cnt+=1
    html.write('</tr>\n')
html.write('</body>\n</html>\n')

