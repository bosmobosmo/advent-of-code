f=open("input.txt")
dat=f.read()
f.close()

f = open('answer.txt', 'w')

line = list(dat)
sum = 0
number = list('0')
negative = False
for i in line:
    try:
        number.append(int(i))
    except:
        if i == '-':
            negative = True
        temp = [str(i) for i in number]
        # print(temp)
        res = int("".join(temp))
        if res > 0:
            # line = [str(sum), '+', str(res), '=']
            # f.write("".join(line))
            if negative:
                sum = sum - res
            else:
                sum = sum + res
            # f.write(str(sum))
            # f.write('\n')
            number = list('0')
            negative = False
        res = 0

print(sum)