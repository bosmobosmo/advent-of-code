from inspect import getcallargs
from itertools import combinations_with_replacement as cwr

from numpy import meshgrid

file = open('input.txt')
data = file.readlines()
file.close()

ingredients = ['F', 'C', 'B', 'S']
capacity = []
durability = []
flavor = []
texture = []
calories = []
recipes = list(cwr(ingredients, 100))
scores = []

def getRecipes(recipe):
    measures = []
    for ingredient in ingredients:
        measures.append(recipe.count(ingredient))
    return measures

def listScore():
    for lines in data:
        line = lines.strip().split(' ')
        capacity.append(int(line[0]))
        durability.append(int(line[1]))
        flavor.append(int(line[2]))
        texture.append(int(line[3]))
        calories.append(int(line[4]))

def getCapacity(measures):
    temp = 0
    for i in range(len(measures)):
        temp = temp + measures[i] * capacity[i]
    if temp <= 0:
        temp = 0
    return temp

def getDurability(measures):
    temp = 0
    for i in range(len(measures)):
        temp = temp + measures[i] * durability[i]
    if temp <= 0:
        temp = 0
    return temp

def getFlavor(measures):
    temp = 0
    for i in range(len(measures)):
        temp = temp + measures[i] * flavor[i]
    if temp <= 0:
        temp = 0
    return temp

def getTexture(measures):
    temp = 0
    for i in range(len(measures)):
        temp = temp + measures[i] * texture[i]
    if temp <= 0:
        temp = 0
    return temp

def getCalories(measures):
    temp = 0
    for i in range(len(measures)):
        temp = temp + measures[i] * calories[i]
    if temp <= 0:
        temp = 0
    return temp

def main():
    
    listScore()
    for recipe in recipes:
        measure = getRecipes(recipe)
        cap = getCapacity(measure)
        dur = getDurability(measure)
        fla = getFlavor(measure)
        tex = getTexture(measure)
        scores.append(cap*dur*fla*tex)

    print(max(scores))
    # best = getRecipes(recipes[scores.index(max(scores))])
    # print(best)
    # bestCapacity = getCapacity(best)
    # bestDurability = getDurability(best)
    # bestflavor = getFlavor(best)
    # besttexture = getTexture(best)

    # print(str(bestCapacity) + ' ' + str(bestDurability) + ' ' + str(bestflavor) + ' ' + str(besttexture))

def second():
    fivehundred = []
    for i in range(len(recipes)):
        measure = getRecipes(recipes[i])
        if (getCalories(measure) == 500):
            fivehundred.append(scores[i])
    print(max(fivehundred))

main()
second()