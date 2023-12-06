file = open('input.txt')
data = file.read().splitlines()
file.close()
file = open('granny.txt')
granny = file.read().splitlines()
file.close()

def criteriaCheck(criteria, candidates):
    passed = []
    for granny in candidates:
        if ((criteria[0] not in granny) or ((criteria[0] + ' ' + criteria[1]) in granny)):
            passed.append(granny)
    return passed

for criteria in granny:
    word = criteria.strip().split(' ')
    data = criteriaCheck(word, data)    

print(data)