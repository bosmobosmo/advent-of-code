f = open('input.txt', 'r')

#part 1
# total = 0
# for line in f:
#     total = total + int(int(line) / 3) - 2

# print (total)

#part 2
def count_fuel(mass):
    fuel = int(mass/3) - 2
    if fuel < 6:
        return fuel
    else:
        return (fuel + count_fuel(fuel))

total = 0
for line in f:
    total = total + count_fuel(int(line))

print (total)