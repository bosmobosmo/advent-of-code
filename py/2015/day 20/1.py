INPUT = 29000000
#900000 too high
#500000 too low
presents = 0
house=500000
while presents < INPUT:
    # print(presents)
    presents = 0
    # house+=1
    factors = []
    print(house)
    for i in range(1, int(house/2)+1):
        if house%i == 0:
            # print('test')
            factors.append(i)
    factors.append(house)
    for elves in factors:
        presents += elves*10
    house+=1
print(house)