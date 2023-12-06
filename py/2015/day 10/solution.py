input = list("3113322113")
# input = list("1")

for i in range(50):
    count = 1
    temp = []
    for j in range(len(input)):
        if j == len(input)-1:
            temp.append(str(count))
            temp.append(input[j])
        elif input[j+1] != input[j]:
            temp.append(str(count))
            temp.append(input[j])
            count = 1
        else:
            count = count + 1
    # print(temp)
    input = temp[:]

# print(input)
print(len(input))