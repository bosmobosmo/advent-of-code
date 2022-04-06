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

def find_status():
    for deer in range(len(deers)):
        if (flight_status[deer] == True):
            if (phase_time[i] > flight[i]):
                phase_time[i] = 0
                flight_status[i] = False
            else:
                phase_time +=1
        else:
            if (phase_time[i] > rest[i]):
                phase_time[i] = 0
                flight_status[i] = True
            else:
                phase_time +=1

def calc_distance(time):
    for i in range(len(deers)):
        if flight_status[i] == True:
            distance[i] += speed[i]
        else:
            distance[i] += 0


# calc_distance(6)
print (deers)
print (speed)
print (flight)
print (rest)
print (phase_time)

for i in range(TIME):
    find_status()
    calc_distance(i+1)


print(distance)