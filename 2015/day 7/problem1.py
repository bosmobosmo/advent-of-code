f=open("input.txt")
dat=f.read()
f.close()

lines=dat.splitlines()
wires = {}



while (len(lines)>0):
    print len(lines)
    # print wires
    for i in lines[:]:
        s = i.split()
        if len(s) == 3:
            # print "masuk s3"
            if s[0].isdigit():
                # print "masuk"
                # print s
                wires[s[2]] = int(s[0]) & 65535

                #problem 2
                if s[2] == 'b':
                    wires['b'] = 3176

                # print wires
                lines.remove(i)
            elif s[0] in wires:
                print i
                # print s
                wires[s[2]] = wires[s[0]] & 65535
                # print wires
                lines.remove(i)
        elif len(s) == 4:
            # print "masuk s4"
            if s[1] in wires:
                # print "masuk"  
                # print s
                wires[s[3]] = ~wires[s[1]] & 65535
                # print wires
                lines.remove(i)
        elif len(s) == 5:
                # print "masuk sh
            if s[1] == 'RSHIFT':
                if s[0] in wires:
                    # print s
                    if s[0] == 'x':
                        print i
                    wires[s[4]] = wires[s[0]] >> int(s[2]) & 65535
                    # print wires
                    lines.remove(i)
            elif s[1] == 'LSHIFT':
                if s[0] in wires:
                    # print s
                    wires[s[4]] = wires[s[0]] << int(s[2]) & 65535
                    # print wires
                    lines.remove(i)
            elif s[1] == 'OR':
                if (s[0] in wires and s[2] in wires):
                    # print s
                    wires[s[4]] = wires[s[0]] | wires[s[2]] & 65535
                    # print wires
                    lines.remove(i)
            elif s[1] == 'AND':
                if s[0].isdigit() and s[2] in wires:
                    # print s
                    wires[s[4]] = int(s[0]) & wires[s[2]] & 65535
                    # print wires
                    lines.remove(i)
                elif (s[0] in wires and s[2] in wires):
                    # print s
                    wires[s[4]] = wires[s[0]] & wires[s[2]] & 65535
                    # print wires
                    lines.remove(i)

# keylist = wires.keys()
# keylist.sort()
# for key in keylist:
#     print "%s : %s" % (key, wires[key])

# wires["dd"] = 40
# wires["bb"] = 50

# if ("bb" and "dd") in wires:
#     print wires["bb"] + wires["dd"]

print wires['a']
# for i in lines:
#     s = i.split()
#     for e in s:
#         if e == 'a':
#             print i
#             continue
#     if len(s) == 5:
#         if s[1] == 'LSHIFT':
#             print s