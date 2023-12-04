from typing import Iterator

NUMERIC_STR = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_puzzle_input() -> Iterator[str]:
    with open("input.txt", "r") as f:
        input = f.read().splitlines()
    for line in input:
        yield line


def get_sum(problem: int) -> None:
    answer = 0
    for line in get_puzzle_input():
        print(f'Line is {line}')
        if problem == 1:
            number = find_numbers(line)
        else:
            number = find_numbers_and_words(line)

        line_number = int(number)
        print(f'number is {line_number}')
        answer += line_number

    print(f'Part {problem} answer is {answer}')


def find_numbers(line: str) -> str:
    numbers = [
        character
        for character in line
        if character.isnumeric()
    ]

    return f'{numbers[0]}{numbers[-1]}'


def find_numbers_and_words(line: str) -> str:
    start_index = len(line)
    end_index = 0
    start = '0'
    end = '0'
    for word, number in NUMERIC_STR.items():
        if word not in line and number not in line:
            continue

        earliest_word = line.find(word) + 1
        earliest_number = line.find(number) + 1
        if earliest_number * earliest_word > 0:
            earliest = min(earliest_word, earliest_number) - 1
        else:
            earliest = max(earliest_word, earliest_number) - 1
        if earliest <= start_index:
            start_index = earliest
            start = number

        latest_word = line.rfind(word)
        latest_number = line.rfind(number)
        latest = max(latest_number, latest_word)
        if latest >= end_index:
            end_index = latest
            end = number

    return f'{start}{end}'


if __name__ == "__main__":
    # get_sum(1)
    get_sum(2)
