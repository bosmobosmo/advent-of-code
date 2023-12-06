from common import parse_command, Operator


def toggle(node: bool) -> bool:
    return node ^ True


def turn_on(node: bool) -> bool:
    return node or True


def turn_off(node: bool) -> bool:
    return not (node or True)


def main() -> None:
    operator = Operator(
        [[False] * 1000 for _ in range(1000)],
        {'toggle': toggle, 'turn_on': turn_on, 'turn_off': turn_off}
    )

    with open('input.txt') as f:
        for string in f.read().splitlines():
            instruction, map = parse_command(string)
            operator.run_instruction(instruction, map)

    active_lights: int = 0
    for x in operator.grid:
        for y in x:
            active_lights += y

    print(f"The number of turned on ligths is {active_lights}")


main()
