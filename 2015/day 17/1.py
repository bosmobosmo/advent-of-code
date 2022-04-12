import collections


file = open('input')
data = file.read().splitlines()
file.close()

#list typecasting
data = list(map(int, data))

EGGNOG = 150
count = 0
cupsused = []

def measure(index, size):
    global count
    size = data[index] + size
    if size == EGGNOG:
        # print(size)
        count = count + 1
    elif size < EGGNOG:
        for i in range(index+1, len(data)):
            measure(i, size)

def measuretwo(index, size, cups):
    global cupsused
    size = data[index] + size
    cups = cups + 1
    if size == EGGNOG:
        cupsused.append(cups)
    elif size < EGGNOG:
        for i in range(index+1, len(data)):
            measuretwo(i, size, cups)

for i in range(len(data)):
    measure(i, 0)

for i in range(len(data)):
    measuretwo(i, 0, 0)

print(count)
print(collections.Counter(cupsused))