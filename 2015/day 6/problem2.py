from common import parse_command, Operator


def toggle(node: int) -> int:
    return node + 2


def turn_on(node: int) -> int:
    return node + 1


def turn_off(node: int) -> int:
    return max((node - 1), 0)


def main() -> None:
    operator = Operator(
        [[0] * 1000 for _ in range(1000)],
        {'toggle': toggle, 'turn_off': turn_off, 'turn_on': turn_on}
    )

    with open('input.txt') as f:
        for string in f.read().splitlines():
            instruction, map = parse_command(string)
            operator.run_instruction(instruction, map)

    intensity: int = 0
    for x in operator.grid:
        for y in x:
            intensity += y

    print(f'Brightness is {intensity}')


main()
