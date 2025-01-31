def main(register_a: int) -> str:
    register_b = 0
    with open("input") as f:
        commands = [line.strip() for line in f.readlines()]
    index = 0
    while True:
        command, input = commands[index].split(" ", maxsplit=1)
        match command:
            case "hlf":
                match input:
                    case "a":
                        register_a /= 2
                    case "b":
                        register_b /= 2
                index += 1
            case "tpl":
                match input:
                    case "a":
                        register_a *= 3
                    case "b":
                        register_b *= 3
                index += 1
            case "inc":
                match input:
                    case "a":
                        register_a += 1
                    case "b":
                        register_b += 1
                index += 1
            case "jmp":
                index = _process_jump(index, input)
            case "jie":
                register, offset = input.split(", ")
                match register:
                    case "a":
                        if register_a % 2 == 0:
                            index = _process_jump(index, offset)
                        else:
                            index += 1
                    case "b":
                        if register_b % 2 == 0:
                            index = _process_jump(index, offset)
                        else:
                            index += 1
            case "jio":
                register, offset = input.split(", ")
                match register:
                    case "a":
                        if register_a == 1:
                            index = _process_jump(index, offset)
                        else:
                            index += 1
                    case "b":
                        if register_b == 1:
                            index = _process_jump(index, offset)
                        else:
                            index += 1
        if index >= len(commands):
            break
    return register_b


def _process_jump(index: int, offset: str) -> int:
    if "+" in offset:
        index += int(offset.removeprefix("+"))
    else:
        index -= int(offset.removeprefix("-"))
    return index

if __name__ == "__main__":
    print(f"Answer to part one is {main(0)}")
    print(f"Answer to part two is {main(1)}")