f=open("input.txt")
dat=f.read()
f.close()

freq = 0
memo = set()
count = 0

lines=dat.splitlines()

while (freq not in memo):
    # print lines[count%len(lines)]
    # print count
    memo.add(freq)
    freq = freq + int(lines[count%len(lines)])
    # memo.sort()
    # print memo
    print len(memo)
    count+=1
    if (freq in memo):
        break
    # print memo

# memo.sort()
# print memo
print freq