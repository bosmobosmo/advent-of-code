PART_ONE_KEYPAD = [
    "123",
    "456",
    "789"
]
PART_TWO_KEYPAD = [
    "00100",
    "02340",
    "56789",
    "0ABC0",
    "00D00"
]

def find_code(keypad: list[list[str]]) -> str:
    with open("input") as f:
        clues = [line.strip() for line in f.readlines()]
    position = [int(len(keypad) / 2), int(len(keypad[0]) / 2)]
    code = ""
    for clue in clues:
        for direction in clue:
            new_pos = position.copy()
            match direction:
                case "L":
                    if position[0] > 0:
                        new_pos[0] -= 1
                case "D":
                    if position[1] < len(keypad) - 1:
                        new_pos[1] += 1
                case "U":
                    if position[1] > 0:
                        new_pos[1] -= 1
                case "R":
                    if position[0] < len(keypad[0]) - 1:
                        new_pos[0] += 1
            if keypad[new_pos[1]][new_pos[0]] != "0":
                position = new_pos.copy()
        code = code + keypad[position[1]][position[0]]
    return code


if __name__ == "__main__":
    print(f"Part one answer is {find_code(PART_ONE_KEYPAD)}")
    print(f"Part two answer is {find_code(PART_TWO_KEYPAD)}")
