f=open('input.txt')
dat=f.read()
f.close()

def toggle(grid, x1, y1, x2, y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            grid[i][j] = grid[i][j] ^ True

def turn_on(grid, x1, y1, x2, y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            # print "Turning on lamp["+str(i)+"]["+str(j)+"]"
            grid[i][j] = True

def turn_off(grid, x1, y1, x2, y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            grid[i][j] = False

# dat = "turn on 499,499 through 500,500"
# dat = ""
grid = [[False] * 1000 for i in range(1000)]
lines = dat.splitlines()

for i in range(len(lines)):
    s = lines[i].split()
    if s[0] == 'toggle':
        one = s[1].split(',')
        x1 = int(one[0])
        y1 = int(one[1])
        two = s[3].split(',')
        x2 = int(two[0])
        y2 = int(two[1])
        toggle(grid, x1, y1, x2, y2)
    else:
        one = s[2].split(',')
        two = s[4].split(',')
        x1 = int(one[0])
        x2 = int(two[0])
        y1 = int(one[1])
        y2 = int(two[1])
        if s[1] == 'on':
            turn_on(grid, x1,y1,x2,y2)
        else:
            turn_off(grid, x1,y1,x2,y2)

count = 0
off = 0

# print grid[500][499]

for i in range(0,1000):
    for j in range(0,1000):
        if grid[i][j] == True:
            count+=1
        # else :
        #     off+=1

# print off
print count