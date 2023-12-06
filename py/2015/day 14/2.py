import numpy as np

file = open('input2.txt')
data = file.readlines()
file.close()
# outfile = open('exout.txt', 'w')

deers = []
speed = []
flight = []
rest = []
flight = []
point = []
distance = []
flight_status = []
phase_time = []
TIME = 2503

for i in range(len(data)):
    line = data[i].strip().split(' ')
    # line[0] = []
    deers.append(line[0])
    speed.append(int(line[1]))
    flight.append(int(line[2]))
    rest.append(int(line[3]))
    flight_status.append(True)
    distance.append(0)
    phase_time.append(0)
    point.append(0)

def find_status():
    for i in range(len(deers)):
        if (flight_status[i] == True):
            if (phase_time[i] > flight[i] - 1):
                # print(phase_time[i])
                phase_time[i] = 1
                flight_status[i] = False
            else:
                phase_time[i] +=1
        else:
            if (phase_time[i] > rest[i] - 1):
                phase_time[i] = 1
                flight_status[i] = True
            else:
                phase_time[i] +=1

def calc_distance():
    for i in range(len(deers)):
        if flight_status[i] == True:
            distance[i] += speed[i]
        else:
            distance[i] += 0

def addPoint():
    front = max(distance)
    # print(front)
    leaders = np.where(np.array(distance) == front)[0]
    for i in leaders:
        point[i] += 1

# calc_distance(6)
# print (deers)
# print (speed)
# print (flight)
# print (rest)

for i in range(TIME):
    find_status()
    calc_distance()
    addPoint()
    # outfile.write('second: ' + str(i+1) + '\n' + deers[0] + ': ' + str(distance[0]) + ', ' + str(flight_status[0]) + '\n' + deers[1] + ': ' + str(distance[1]) + ', ' + str(flight_status[1]) + '\n')

# outfile.close()
print(point)