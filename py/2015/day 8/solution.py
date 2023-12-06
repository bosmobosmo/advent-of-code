f=open("input.txt")
dat=f.read()
f.close()

lines = dat.splitlines()
count = 0

for line in lines:
    #count = count + len(line)
    temp = 0
    i = 0
    while (i<len(line)):
    # Problem 1
    #     if line[i] == '\\':
    #         if (line[i+1] == '\"' or line[i+1] == '\\'):
    #             temp = temp+1
    #             i = i+2
    #             continue
    #         elif line[i+1] == 'x':
    #             temp = temp+1
    #             i = i+4
    #             continue
    #         temp = temp + 1
    #     temp = temp + 1
    #     i = i + 1
    # temp = temp - 2
    # print temp
    # count = count - temp

    # Problem 2
        temp+=1
        if line[i] == '\"':
            temp+=1
        if line[i] == '\\':
            temp+=1
        i+=1
    temp+=2
    temp = temp - len(line)
    count+=temp

print count