

def main() -> None:
    with open('input', 'r') as f:
        input = f.read().splitlines()
    part_1(input)
    part_2(input)


def part_1(input: list[str]) -> None:
    biggest_calories = 0
    current_calories = 0
    for line in input:
        if line == '':
            biggest_calories = current_calories \
                if current_calories > biggest_calories \
                else biggest_calories
            current_calories = 0
        else:
            current_calories = current_calories + int(line)

    print(f"Part 1 answer is {biggest_calories}")


def part_2(input: list[str]) -> None:
    elves_calories = []
    current_calories = 0

    for line in input:
        if line == '':
            elves_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories = current_calories + int(line)

    big_three = 0
    for i in range(3):
        big_three = big_three + elves_calories.pop(
            elves_calories.index(
                max(elves_calories)
            )
        )
    
    print(f'Part 2 answer is {big_three}')


main()
