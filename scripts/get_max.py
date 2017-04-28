# This script aims to find out the maximum value among all the .raw files. The result can be further used in normalize the .raw and write reasonable .wav from them.
# The currently max_value found is 43.6791.

import os

max_value = 0.0
for sceneID in range(1000,1022,1):
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
                    rawFile = open(os.path.join(son,toy),"r")
                    for line in rawFile:
                        if max_value < abs(float(line.split()[0])):
                            max_value = abs(float(line.split()[0]))
                            print(max_value)
                    rawFile.close()
