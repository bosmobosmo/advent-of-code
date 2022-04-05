file = open('input2.txt')
data = file.readlines()
file.close()

record = {}
TIME = 2503

# print(type(data))

for lines in data:
    line = lines.strip().split(' ')
    # print(line)
    name = line[0]
    flight = int(line[2])
    dist = int(line[1])
    rest = int(line[3])
    distance1 = int(TIME / (flight+rest)) * flight * dist
    # print(flight+rest)
    leftover = TIME % (flight+rest)
    if leftover <= flight:
        distance2 = leftover * dist
    else:
        distance2 = flight * dist
    total = distance1+distance2
    record[name] = total

print(dict(sorted(record.items(), key=lambda item:item[1])))