# This script get the maximum value in each .raw file and the portion of bad sound of each scene
import os
import threading

def check(sceneID):
    print("Checking scene-"+str(sceneID))
    file_out = open("/data/vision/billf/object-properties/sound/qiujiali/sound/sound_info/sound-"+str(sceneID)+".txt","w")
    file_out.write("                                                          \n")
    num_good = 0
    num_bad = 0
    grandpa = os.path.join(".","scene-"+str(sceneID))
    papas = os.listdir(grandpa)
    for papa in papas:
        father = os.path.join(grandpa,papa)
        puppies = os.listdir(father)
        for puppy in puppies:
            son = os.path.join(father,puppy)
            toys = os.listdir(son)
            for toy in toys:
                if toy[-3:]=='raw':
                    max_value = 0.0
                    rawFile = open(os.path.join(son,toy),"r")
                    for line in rawFile:
                        if max_value < abs(float(line.split()[0])):
                            max_value = abs(float(line.split()[0]))
                    file_out.write(str(os.path.join(son,toy))+" "+str(max_value)+"\n")
                    if max_value > 1.0:
                        num_bad+=1
                    else:
                        num_good+=1
                    rawFile.close()
    file_out.seek(0)
    file_out.write(str(num_good)+" "+str(num_bad))
    file_out.close()
    print("Finished scene-"+str(sceneID))

threads = []
for ID in range(1000,1022,1):
    threads.append(threading.Thread(target=check, args=(ID,)))
for t in threads:
    t.start()
for t in threads:
    t.join()
