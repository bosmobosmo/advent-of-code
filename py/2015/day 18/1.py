file = open('input')
data = file.read().splitlines()
file.close()

config = []

#make array
for i in range(len(data)):
    line = []
    line[:0] = data[i]
    config.append(line)

# print(len(config[0]))

def decideState(x, y):
    state = config[x][y]
    lights = neighbour(x,y)
    if state == '.':
        if lights == 3:
            return '#'
        else:
            return '.'
    else:
        if ((lights < 2) or (lights > 3)):
                # print(tes)
            return '.'
        else:
            return '#'

def neighbour(x,y):
    # print(str(x) + ' ' + str(y))
    on = 0
    for indexX in range(x-1, x+2):
        if ((indexX < 0) or (indexX+1) > len(config)):
            # print(indexX)
            continue
        for indexY in range(y-1, y+2):
            # print(str(indexX) + ' ' + str(indexY))
            if ((indexY < 0) or (indexY+1) > len(config[x])):
                # print(len(config[x]))
                # print(str(indexX) + ' ' + str(indexY))
                continue
            if ((indexX == x) and (indexY == y)):
                continue
            elif (config[indexX][indexY] == '#'):
                # print('on')
                on += 1
    return on

config[99][0] = '#' #fix for number 2 input
# print(neighbour (0,0))
for i in range(100):
    # print(i)
    newconfig = []
    for ix in range(len(config)):
        line = []
        for iy in range(len(config[ix])):
            line.append(decideState(ix, iy))
        newconfig.append(line)
    for j in [0,len(config)-1]:
        for k in [0, len(config)-1]:
            newconfig[j][k] = '#' #number 2
    config = newconfig[:]
# print(neighbour(4,0))
on = 0
for i in range(len(config)):
    for j in range(len(config[i])):
        if (config[i][j] == '#'):
            on +=1
file = open('output', 'w')
for ix in newconfig:
    # print(len(ix))
    for iy in ix:
        # print(len(iy))
        file.write(str(iy))
    file.write('\n')
file.close()
print(on)