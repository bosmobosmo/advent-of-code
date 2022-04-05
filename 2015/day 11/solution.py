input = list('cqjxjnds')

def first_req(pwd):
    # print("first req")
    seq = False
    for i in range(len(pwd) - 2):
        if pwd[i+1] - pwd[i] == 1 and pwd[i+2] - pwd[i+1] == 1:
            seq = True
    return seq

def second_req(pwd):
    # print('2')
    iol = False
    for i in pwd:
        if i == ord('i'):
            iol = True
        elif i == ord('o'):
            iol = True
        elif i == ord('l'):
            iol = True
    return iol

def third_req(pwd):
    # print("3")
    pairs = 0
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i+1] and pwd[i] != pwd[i-1]:
            pairs = pairs + 1
    if pairs > 1:
        return True
    else:
        return False

def req(pwd):
    first = first_req(pwd)
    second = second_req(pwd)
    third = third_req(pwd)
    return (first and not(second) and third)

def newpass(pwd, index):
    new = pwd[index]
    if new == ord('z'):
        pwd = newpass(pwd, index-1)
        new = ord('a')
    else:
        new = new+1
    pwd[index] = new
    return pwd

password = []
pwd = []

for i in input:
    pwd.append(ord(i))

# print(first_req(pwd))

while req(pwd) == False:
    pwd = newpass(pwd, len(pwd) -1)
    # password = []
pwd = newpass(pwd, len(pwd) - 1)

while req(pwd) == False:
    pwd = newpass(pwd, len(pwd) -1)

for i in pwd:
    password.append(chr(i))
print(password)

# input = list("cqjxxyzz")
# for i in input:
#     pwd.append(ord(i))

# print(req(pwd))