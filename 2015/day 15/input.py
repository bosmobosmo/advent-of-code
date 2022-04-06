file = open('input.txt')
data = file.readlines()
file.close()
outfile = open('input.txt', 'w')

for line in data:
    word = line.strip().split(' ')
    outfile.write(word[2][:-1] + ' ' + word[4][:-1] + ' ' + word[6][:-1] + ' ' + word[8][:-1] + ' ' + word[10] + '\n')

outfile.close()