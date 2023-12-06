INPUT = 29000000

house = []
for i in range (int(INPUT/10)+2): #list initialization
    house.append(0)
print('test')
for i in range(1, int(INPUT/10)+1):
    # print(i)
    j = i
    visit = 50
    while((visit > 0) and (j<int(INPUT/10)+1)):
        house[j] += i*11
        j+=i
        visit -=1
i=1
presents = 0
while True:
    presents = house[i]
    if presents >= INPUT:
        break
    i+=1
print(i)