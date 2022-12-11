def main() -> None:
    with open('input', 'r') as f:
        input = f.read().splitlines()

    part_one(input)
    part_two(input)


def get_priority(item: str) -> int:
    if item.islower():
        #  ord a is 97
        return ord(item) - 96
    else:
        #  ord A is 65
        return ord(item) - 38


def part_one(input: str) -> None:
    sum = 0
    for rucksack in input:
        half = int(len(rucksack)/2)
        first = rucksack[:half]
        second = rucksack[half:]
        
        for item in first:
            if item in second:
                break

        sum = sum + get_priority(item)

    print(f'Part 1 answer is {sum}')


def part_two(input: str) -> None:
    sum = 0
    index = 0
    group: list[str] = ['', '', '']
    for rucksack in input:
        group[index] = rucksack
        if index == 2:
            for item in rucksack:
                if item in group[1] and item in group[0]:
                    sum = sum + get_priority(item)
                    break
            index = 0
        else:
            index = index + 1

    print(f'Part 2 answer is {sum}')


main()