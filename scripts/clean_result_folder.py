import os
import subprocess
RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/result'
ROOT = '/data/vision/billf/object-properties/sound/sound'
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def CreateDir(path):
    if not os.path.exists(path):
        os.makedirs(path)



def GetEntry():
	obj_list_path= '/data/vision/billf/object-properties/sound/sound/data/final100/small_stats.txt'
	mat_matrix_path  = '/data/vision/billf/object-properties/sound/sound/data/material_matrix.dat'
	obj_list_file = open(obj_list_path,'r')
	mat_matrix_file = open(mat_matrix_path,'r')
	task_list = dict()
	cnt = 0
	for line in obj_list_file.readlines():
	    obj_id = int(line.split()[0])
	    task_list[obj_id] = []
	for line in mat_matrix_file.readlines():
	    data = line.split()
	    obj_id = int(data[0])
	    if not obj_id in task_list:
	        continue
	    else:
	        for k in range(1,len(data)):
	            if data[k]=='1' and k<=8 and k!=6:
	                target_dir = '/data/vision/billf/object-properties/sound/sound/result/scene-1000/obj-101-%d/mat-4-%d/obj-%04d.wav'\
				%(obj_id,k-1,obj_id)
	                if os.path.exists(target_dir):
	                    task_list[obj_id].append(k-1)
	                    cnt+=1
	print cnt


	scene_entry = '/data/vision/billf/object-properties/sound/sound/config/scene/stat.txt'
	scene_args = open(scene_entry,'r')
	render_cmd = []
	audio_ready = []
	video_ready = []
	ready = []
	for line in scene_args.readlines():
		#print line
		sceneid = int(line.split()[0])
		args = line.split()[1:]
		#print args
		flag = 0
		objs = []
		mats = []
		for x in range(len(args)/2):

			obj_id = int(args[x*2])
			mat_id = int(args[x*2+1])

			objs.append(obj_id)
			mats.append(mat_id)
			if obj_id<=100:
				target_dir = '/data/vision/billf/object-properties/sound/sound/data/final100/%d/models/mat-%d/moments/moments.pbuf'\
				%(obj_id,mat_id)
				#print target_dir
				if not os.path.exists(target_dir) or mat_id==5:
					flag = 1
				if mat_id==5:
					flag==1
					#print "5!!!!"
				if not obj_id in task_list.keys():
					flag = 1
					#print "obj!!!!!"
				elif not mat_id in task_list[obj_id]:
					flag = 1
					#print "mat!!!!!!"
					#print obj_id,mat_id
		if flag==0:
			render_cmd.append(line)
	ROOT = '/data/vision/billf/object-properties/sound/sound/'
	scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.1.txt')).readlines()
	cnt = 0
	for entry in scene_entry:
		if entry in render_cmd:
			#print"COLLISION!!!!!"
			cnt+=1
		else:
			render_cmd.append(entry)
	print cnt
	print(len(render_cmd))
	return render_cmd


def RenderCmd2Dict(render_cmd):
	check_list = dict()
	for line in render_cmd:
		args_orig = line.split()
		sceneid = int(args_orig[0])
		scene_dir = "scene-%d"%sceneid
		args = args_orig[1:]
		objs = []
		mats = []
		for x in range(len(args)/2):
			obj_id = int(args[x*2])
			mat_id = int(args[x*2+1])
			objs.append(obj_id)
			mats.append(mat_id)
		objdir = "obj"
		matdir = "mat"
		for objid in range(len(objs)):
			objdir+="-%d"%(objs[objid])
		for matid in range(len(mats)):
			matdir+='-%d'%(mats[matid])
		if not scene_dir in check_list:
			check_list[scene_dir]=dict()
		if not objdir in check_list[scene_dir]:
			check_list[scene_dir][objdir] = []
		if not matdir in check_list[scene_dir][objdir]:
			check_list[scene_dir][objdir].append(matdir)
		else:
			print "COLLISION!!!"
	return check_list

def CleanResult(check_list,result_root):
	scene_level_dir = os.listdir(result_root)
	#print scene_level_dir
	obj_cnt_r = 0
	obj_cnt = 0
	mat_cnt = 0
	mat_cnt_r =0
	with cd(result_root):
		for scene_folder in scene_level_dir:
			if scene_folder not in check_list:
				print scene_folder
				subprocess.call('mv %s ./../to_be_deleted'%(scene_folder),shell='True')
			else:
				obj_level_dir = os.listdir(os.path.join(result_root,scene_folder))
				for obj_folder in obj_level_dir:
					if obj_folder not in check_list[scene_folder]:
						subprocess.call('mkdir -p ./../to_be_deleted/%s'%(scene_folder),shell='True')
						subprocess.call('mv %s ./../to_be_deleted/%s'%(os.path.join(scene_folder,obj_folder),scene_folder),shell='True')
						obj_cnt_r +=1
					else:
						mat_level_dir = os.listdir(os.path.join(result_root,scene_folder,obj_folder))
						for mat_folder in mat_level_dir:
							if mat_folder not in check_list[scene_folder][obj_folder]:
								subprocess.call('mkdir -p ./../to_be_deleted/%s/%s'%(scene_folder,obj_folder),shell='True')
								subprocess.call('mv %s ./../to_be_deleted/%s/%s/'%(os.path.join(scene_folder,obj_folder,mat_folder),scene_folder,obj_folder),shell='True')
								mat_cnt_r +=1
							else:
								mat_cnt+=1

						#print obj_folder
	print obj_cnt,obj_cnt_r
	print mat_cnt,mat_cnt_r


render_cmd = GetEntry()
check_list = RenderCmd2Dict(render_cmd)
CleanResult(check_list,RESULT_ROOT)
cnt = 0
for k in check_list.keys():
	for k2 in check_list[k]:
		for v3 in check_list[k][k2]:
			cnt+=1
print cnt


