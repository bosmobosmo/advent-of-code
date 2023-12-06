f = open('input.txt','r')

for line in f:
    opcode = line.split(',')
    
setopcode = [int(x) for x in opcode]

#part 1
# i = 0
# opcode[1] = 12
# opcode[2] = 2
# while opcode[i] != 99:
#     # print(i)
#     # print (opcode[i])
#     if opcode[i] == 1:
#         temp = opcode[opcode[i+1]] + opcode[opcode[i+2]]
#         opcode[opcode[i+3]] = temp
#         i = i+4
#     elif opcode[i] == 2:
#         temp = opcode[opcode[i+1]] * opcode[opcode[i+2]]
#         opcode[opcode[i+3]] = temp
#         i = i+4
#     else:
#         print("error")

# print(opcode[0])

#part 2
i = 0
for n in range(100):
    for v in range(100):
        i = 0
        opcode = setopcode.copy()
        opcode[1] = int(n)
        opcode[2] = int(v)
        while opcode[i] != 99:
            if opcode[i] == 1:
                temp = opcode[opcode[i+1]] + opcode[opcode[i+2]]
                opcode[opcode[i+3]] = temp
                i = i+4
            elif opcode[i] == 2:
                temp = opcode[opcode[i+1]] * opcode[opcode[i+2]]
                opcode[opcode[i+3]] = temp
                i = i+4
        if opcode[0] == 19690720:
            print(100 * int(n) + int(v))