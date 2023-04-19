from typing import NamedTuple, TypeVar

T = TypeVar('T')
array = list[list[bool]]


class InstructionMap(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int


def run_instruction(
    grid: array, instruction: str, map: InstructionMap
) -> array:
    match instruction:
        case 'toggle':
            operation = toggle
        case 'on':
            operation = turn_on
        case 'off':
            operation = turn_off
        case _:
            raise NotImplementedError()
    # print(grid)
    for x in range(map.x1, map.x2 + 1):
        for y in range(map.y1, map.y2 + 1):
            grid[x][y] = operation(grid[x][y])
    # print(grid)
    return grid


def toggle(node: bool) -> bool:
    return node ^ True


def turn_on(node: bool) -> bool:
    return node or True


def turn_off(node: bool) -> bool:
    return not (node or True)


def parse_command(input: str) -> tuple[str, InstructionMap]:
    command = input.lower().split(' ')
    if 'turn' in command:
        command.remove('turn')
    command.remove('through')
    instruction = command[0]
    x1, y1 = command[1].split(',')
    x2, y2 = command[2].split(',')
    return instruction, InstructionMap(int(x1), int(y1), int(x2), int(y2))


def main() -> None:
    grid = [[False] * 1000 for _ in range(1000)]

    with open('input.txt') as f:
        for string in f.read().splitlines():
            instruction, map = parse_command(string)
            grid = run_instruction(grid, instruction, map)

    active_lights = 0
    for x in grid:
        for y in x:
            active_lights += y

    print(f"The number of turned on ligths is {active_lights}")


main()
