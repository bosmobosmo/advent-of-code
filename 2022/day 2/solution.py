import enum




def main() -> None:
    with open('input', 'r') as f:
        input = f.read().splitlines()
    part_one(input)
    part_two(input)


def part_one(input: list[str]) -> None:
    score_gain = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    point_gain = {
        '0': ['A Z', 'B X', 'C Y'],
        '3': ['A X', 'B Y', 'C Z'],
        '6': ['A Y', 'B W', 'C X',],
    }
    def _score_gained(match: str) -> int:
        for point, pattern in point_gain.items():
            if match in pattern:
                break

        return int(point) + score_gain[match.split(' ')[1]]

    score = 0
    for line in input:
        score = score + _score_gained(line)

    print(f'Part 1 answer is {score}')


def part_two(input: list[str]) -> None:
    score_gain = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    point_gain = {
        '1': ['A Y', 'B X', 'C Z'],
        '2': ['A Z', 'B Y', 'C X'],
        '3': ['A X', 'B Z', 'C Y'],
    }
    def _score_gained(match: str) -> int:
        for point, pattern in point_gain.items():
            if match in pattern:
                break

        return int(point) + score_gain[match.split(' ')[1]]

    score = 0
    for line in input:
        score = score + _score_gained(line)

    print(f'Part 2 answer is {score}')


main()
