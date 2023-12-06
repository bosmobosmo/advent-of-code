INPUT = 29000000

house = []
for i in range (int(INPUT/10)+2): #list initialization
    house.append(0)
print('test')
for i in range(1, int(INPUT/10)+1):
    # print(i)
    j = i
    while(j < INPUT/10):
        house[j] += i*10
        j+=i
i=1
presents = 0
while True:
    presents = house[i]
    if presents >= INPUT:
        break
    i+=1
print(i)