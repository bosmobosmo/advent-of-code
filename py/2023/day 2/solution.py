from pathlib import Path
from typing import Iterator

# from common import get_input

THRESHOLD = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_input(path: str) -> Iterator[str]:
    with open(path, "r") as f:
        input = f.read().splitlines()
    for line in input:
        yield line


def check_game(input: str) -> bool:
    for set in input.strip().split(';'):
        for ball in set.strip().split(', '):
            count, color = ball.split(' ')
            if int(count) > THRESHOLD[color]:
                return False
    return True


def problem1() -> None:
    answer = 0
    input_path = Path("./input.txt").absolute()
    for line in get_input(str(input_path)):
        game_id, input = line.split(':')
        game_id = game_id.split(' ')[-1]
        if check_game(input):
            answer += int(game_id)

    print(f'problem 1 answer is {answer}')


def problem2() -> None:
    answer = 0
    input_path = Path("./input.txt").absolute()
    for line in get_input(str(input_path)):
        input = line.split(':')[-1]
        balls_count: dict[str, int] = {}
        for set in input.strip().split(';'):
            # print(set)
            for ball in set.strip().split(', '):
                count, color = ball.split(' ')
                if balls_count.get(color, 0) > int(count):
                    continue
                balls_count[color] = int(count)
        power = 1
        print(input)
        print(balls_count)
        for count2 in balls_count.values():
            power = power * count2
        print(power)
        answer += power
    print(f'problem 2 answer is {answer}')


problem1()
problem2()
