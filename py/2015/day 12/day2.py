import json

with open('input.json') as json_file:
    data = json.load(json_file)

def loop(item):
    if type(item) == int:
        return item
    elif type(item) == list:
        value = 0
        for n in item:
            value += loop(n)
        return value
    elif type(item) == dict:
        if 'red' in item.values() or "red" in item:
            return 0
        value = 0
        for n in item:
            value += loop(n)
            value += loop(item[n])
        return value
    else:
        return 0

total = 0
total += loop(data)

print(total)