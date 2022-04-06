file = open('input2.txt')
data = file.readlines()
file.close()

deers = []
speed = []
flight = []
rest = []
flight = []
point = []
distance = []
TIME = 2503

# def find_status(time):
#     for i in range(len(deers)):
#         if 

def calc_distance(time):
    for i in range(len(deers)):
        if ((time+1)%(flight[i]+rest[i]) > flight[i]):
            distance[i] +=0
        else:
            distance[i] += speed[i]

for i in range(len(data)):
    line = data[i].strip().split(' ')
    # line[0] = []
    deers.append(line[0])
    speed.append(int(line[1]))
    flight.append(int(line[2]))
    rest.append(int(line[3]))
    # flight.append(True)
    distance.append(0)

calc_distance(135)

# for i in range(TIME):
#     calc_distance(i)


print (deers)
print (speed)
print (flight)
print (rest)
print(distance)