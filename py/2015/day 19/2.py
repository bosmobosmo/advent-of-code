import re
#program won't stop for some reason
#that's why I put print answer inside the function

file = open("input")
data = file.read().splitlines()
file.close()
# file = open('output', 'w')
counters = []
finalproducts = []
base = []
configs = []
i = 0
while (len(data[i]) > 0):
    conv=data[i].split(' ')
    conv.reverse()
    # print(conv)
    if(conv[0] not in base):
        base.append(conv[0])
    del conv[1]
    configs.append(conv)
    i+=1
MOLECULE = data[len(data) - 1]
# print(len(re.findall('[A-Z]',MOLECULE)))
# print(base)

def reduce(sample, counter):
    for b in base:
        instances = [m.start() for m in re.finditer(b, sample)] #list of index with b in current sample
        if len(instances) == 0:
            continue
        else:
            for i in instances:
                counter+=1
                # j = int(i)
                for c in configs:
                    if c[0] == b:
                        next = []
                        next.append(sample[:i])
                        next.append(c[1])
                        next.append(sample[i+len(c[0]):])
                        next = ''.join(next)
                        # file.write(c[0] + ' ' + str(i) + '\n' + next + '\n')
                        if len(next)>2:
                            reduce(next, counter)
                        elif next=='e':
                            counters.append(counter)
                            print(min(counters))
                        else:
                            continue

def synthesis(sample, counter):
    for b in base:
        instances = [m.start() for m in re.finditer(b, sample)] #list of index with b in current sample
        # print(instances)
        if len(instances) > 0:
            for i in instances:
                counter+=1
                j = int(i)
                for c in configs:
                    if c[0] == b:
                        next = []
                        next.append(sample[:j])
                        next.append(c[1])
                        next.append(sample[j+len(c):])
                        next = ''.join(next)
                        # print(next)
                        if len(next) >= len(MOLECULE):
                            finalproducts.append(next)
                            counters.append(counter)
                        else:
                            synthesis(next, counter)
# goodcounter = []
reduce(MOLECULE, 0)
# for i in range(len(finalproducts)):
#     if (finalproducts[i] == MOLECULE):
#         goodcounter.append(counters[i])
# file.close()