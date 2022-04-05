import itertools

count = 0

letters= "ABC"
combo = list(itertools.permutations(letters, 3))
print(len(combo))
for i in combo:
    print(i)