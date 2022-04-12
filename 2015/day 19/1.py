import collections
import re
import string


file = open("input")
data = file.read().splitlines()
file.close()


configs = []
i = 0
while (len(data[i]) > 0):
    configs.append(data[i])
    i+=1
molecule = data[len(data) - 1]

configlist = []
for i in configs:
    conv = []
    word = i.split(' ')
    conv.append(word[0])
    conv.append(word[2]) 
    configlist.append(conv)

newmolecules = []
for conversion in configlist:
    size = len(conversion[0])
    instances = [m.start() for m in re.finditer(conversion[0], molecule)]
    if len(instances) > 0:
        for i in instances:
            newmolecule = []
            j = int(i)  
            newmolecule.append(molecule[:j])
            newmolecule.append(conversion[1])
            newmolecule.append(molecule[j+size:])
            newmolecule = ''.join(newmolecule)
            newmolecules.append(newmolecule)

print(len(dict.fromkeys(newmolecules)))