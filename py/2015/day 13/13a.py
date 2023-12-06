from itertools import permutations, combinations

file = open('input.txt')
data = file.readlines()
file.close()
outfile = open('test.txt', 'w')

people = []
simple = []
weighted_pair = []

def simplify(line):
    word = line.strip().split(' ')
    value = int(word[3])
    if word[2] == 'lose':
        value = value * -1
    if word[0] not in people:
        people.append(word[0])
    return [word[0], word[10][:-1], value]

def problem2():
    # people.append('me')
    for i in people:
        weighted_pair.append([i, 'Me', 0])
    people.append('Me')

def find_value(seating):
    happiness = 0
    # pairs = combinations(seating, 2)
    for i in range(len(seating)):
        # print(i)
        # outfile.write(seating[i] + ' ' + seating[(i+1)%len(seating)] + '\n')
        for p in weighted_pair:
            if ((seating[i] in p) and (seating[(i+1)%len(seating)] in p)):
                outfile.write(seating[i] + ' ' + seating[(i+1)%len(seating)] + ' ' + str(p[2]) + '\n')
                happiness += p[2]
    return happiness

def pairing_value(pair):
    happiness = 0
    for i in simple:
        if (i[0]in pair) and (i[1] in pair):
            happiness+=i[2]
            # print(happiness)
    # print(happiness)
    return happiness    

for line in data:
    simple.append(simplify(line))

pairing = combinations(people, 2)

for i in pairing:
    i = list(i)
    i.append(pairing_value(i))
    weighted_pair.append(i)
    # print(i)
    # outfile.write(str(i) + '\n')

problem2()

schemes = list(permutations(people, len(people)))
# for i in simple:
#     outfile.write(str(i) + '\n')

for i in weighted_pair:
    outfile.write(str(i) + '\n')

ultimateHappiness = 0
lHappiness = 0

# print(find_value(['Alice','Bob','David']))
# print(len(schemes))
for i in schemes:
    sHappiness = find_value(i)
    ultimateHappiness = max(ultimateHappiness, sHappiness)
    # if lHappiness != ultimateHappiness:
    outfile.write(str(i) + ' ' + str(sHappiness) + '\n')
        # lHappiness = ultimateHappiness

print(ultimateHappiness)
outfile.close()

