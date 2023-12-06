file = open('input.txt')
data = file.readlines()
file.close()
outfile = open('input2.txt', 'w')

for line in data:
    word = line.strip().split(' ')
    outfile.write(word[0] + ' ' + word[3] + ' ' + word[6] + ' ' + word[13] + '\n')

outfile.close()