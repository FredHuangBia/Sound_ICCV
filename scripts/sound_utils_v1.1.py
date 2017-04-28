import os
import subprocess

RESULT_ROOT = '/data/vision/billf/object-properties/sound/sound/result_v1_1'
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

class Entry:
	def __init__(self,line):
		self.entry = line
		self.Load(line)
	def __eq__(self, other):
		return self.entry==other.entry
	def Stat(self,verbose=False):
		self.isAudioReady = self.IsAudioReady(verbose)
		self.isVideoReady = self.IsVideoReady(verbose)
		self.isRawReady = self.IsRawReady(verbose)
		self.isReady = self.isRawReady and self.isVideoReady and self.isAudioReady
		self.isResultReady = self.IsResultReady(verbose)
	def Load(self,line):
		sceneid = int(line.split()[0])
		args = line.split()[1:]
		flag = 0
		objs = []
		mats = []
		for x in range(len(args)/2):

			obj_id = int(args[x*2])
			mat_id = int(args[x*2+1])

			objs.append(obj_id)
			mats.append(mat_id)
		self.scene = sceneid
		self.objs = objs
		self.mats = mats
		scenedir = 'scene-%d'%self.scene
		objdir = "obj"
		matdir = "mat"
		for objid in range(len(objs)):
			objdir+="-%d"%(objs[objid])
		for matid in range(len(mats)):
			matdir+='-%d'%(mats[matid])
		self.path = os.path.join(RESULT_ROOT,scenedir,objdir,matdir)
		self.result = os.path.join(self.path,'result.mp4')
		self.audio = dict()
		self.raw = dict()
		for obj in self.objs:
			if obj>=100:
				continue
			else:
				self.audio[obj] = os.path.join(self.path,'obj-%04d.wav'%obj)
				self.raw[obj] =os.path.join(self.path,'obj-%04d.raw'%obj)
		self.video = os.path.join(self.path,'sli.mp4')

	def IsAudioReady(self,verbose=False):
		flag = 0
		if verbose:
			print self.path
		for obj in self.objs:
			if obj>=100:
				continue
			else:
				if not os.path.exists(os.path.join(self.path,'obj-%04d.wav'%obj)):
					flag = 1
					if verbose:
						print "         %s: not ready"%obj
				else:
					if verbose:
						print "         %s: ready"%obj
		if flag==0:
			return True
	def IsRawReady(self,verbose=False):
		flag = 0
		if verbose:
			print self.entry
		for obj in self.objs:
			if obj>=100:
				continue
			else:
				if not os.path.exists(os.path.join(self.path,'obj-%04d.raw'%obj)):
					flag = 1
					if verbose:
						print "         %s: not ready"%obj
				else:
					if verbose:
						print "         %s: ready"%obj
		if flag==0:
			return True



	def IsVideoReady(self,verbose=False):
		if os.path.exists(os.path.join(self.path,'sli.mp4')):
			if verbose:
				print '%s: video ready!\n'%self.entry
			return True
		else:
			return False

	def IsResultReady(self,verbose=False):
		if os.path.exists(os.path.join(self.path,'result.mp4')):
			if verbose:
				print '%s: result ready!\n'%self.entry
			return True
		else:
			return False

	def MatsToString(self):
		matstr = ""
		for x in range(len(self.mats)):
			matstr+="%d "%self.mats[x]
		return matstr

	def ObjsToString(self):
		objstr = ""
		for x in range(len(self.objs)):
			objstr+="%d "%self.objs[x]
		return objstr



def GetEntryV1():
	entry = []
	scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.txt')).readlines()
	for line in scene_entry:
		entry.append(Entry(line))
	print(len(entry))
	return entry

def GetEntryV1_1():
	entry = GetEntryV1()
	entryv1_1=[]
	scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.1.txt')).readlines()
	cnt = 0
	for line in scene_entry:
		cur = Entry(line)
		if cur in entry:
			#print"COLLISION!!!!!"
			cnt+=1
		else:
			entryv1_1.append(cur)
	#print cnt
	print(len(entryv1_1))
	return entryv1_1

def GetEntry():
	entry = GetEntryV1()
	scene_entry = open(os.path.join(ROOT,'config','scene','stat_v1.1.txt')).readlines()
	cnt = 0
	for line in scene_entry:
		cur = Entry(line)
		if cur in entry:
			#print"COLLISION!!!!!"
			cnt+=1
		else:
			entry.append(cur)
	#print cnt
	print(len(entry))
	return entry

def PartitionCmd(render_cmd,m):
	task = dict()
	cnt = 0
	for x in range(0,len(render_cmd)):
		if cnt>=m:
			cnt=0
		if cnt not in task:
			task[cnt] = []
		task[cnt].append(render_cmd[x])
		#print cnt
		cnt+=1
	return task

def GetVidLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]







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

def CleanResult_V1_1(check_list,result_root):
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


