import re

file = open('input.txt')
data = file.read().splitlines()
file.close()
file = open('granny.txt')
granny = file.read().splitlines()
file.close()

def criteriaCheck(criteria, candidates):
    passed = []
    for granny in candidates:
        # print(type(granny))
        temp = re.sub(',','',granny)
        individual = temp.strip().split(' ')
        if (criteria[0] not in individual):
            passed.append(granny)
        elif ((criteria[0] == 'cats:') or (criteria[0] =='trees:')):
            category = individual.index(criteria[0])
            # print(granny)
            # print(category)
            if (int(individual[category+1]) > int(criteria[1]) ):
                passed.append(granny)
        elif ((criteria[0] == 'goldfish:') or (criteria[0] == 'pomeranians:')):
            category = individual.index(criteria[0])
            if (int(individual[category+1]) < int(criteria[1])):
                # print(granny)
                passed.append(granny)
        elif ((criteria[0] in individual) and (criteria[1] == individual[individual.index(criteria[0]) + 1])):
            passed.append(granny)
    return passed

for criteria in granny:
    word = criteria.strip().split(' ')
    # print(word)
    data = criteriaCheck(word, data)    

print(data)