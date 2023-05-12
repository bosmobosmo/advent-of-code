from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Sequence, Union

InputType = Sequence[str]
LogicGate = Callable[[InputType], int]
CIRCUIT: dict[str, Union[Command, int]] = {}


@dataclass
class Command:
    gate: LogicGate
    inputs: InputType


def bitwise_and(inputs: InputType) -> int:
    this_input = [
        int(input)
        if input.isdigit()
        else get_output(input)
        for input in inputs
    ]
    return this_input[0] & this_input[1]


def bitwise_or(inputs: InputType) -> int:
    this_input = [
        int(input)
        if input.isdigit()
        else get_output(input)
        for input in inputs
    ]
    return this_input[0] | this_input[1]


def bitwise_not(inputs: InputType) -> int:
    input = get_output(inputs[0])
    return ~input


def bitwise_lshift(inputs: InputType) -> int:
    steps = int(inputs[1])
    input = get_output(inputs[0])
    return input << steps


def bitwise_rshift(inputs: InputType) -> int:
    steps = int(inputs[1])
    input = get_output(inputs[0])
    return input >> steps


def direct_assignment(inputs: InputType) -> int:
    if inputs[0].isdigit():
        input = int(inputs[0])
    else:
        input = get_output(inputs[0])
    return input


def get_output(input: str) -> int:
    stored_value = CIRCUIT.get(input)
    if stored_value is None:
        raise Exception("Command not found")
    if isinstance(stored_value, int):
        return stored_value
    output = stored_value.gate(stored_value.inputs)
    CIRCUIT[input] = output
    return output


def main() -> None:
    with open('input.txt') as f:
        for instruction in f.read().splitlines():
            command, output = _parse_instruction(instruction)
            CIRCUIT[output] = command
    print(get_output('a'))


def _parse_instruction(instruction: str) -> tuple[Command, str]:
    words = instruction.split(" ")
    if len(words) == 3:
        return Command(direct_assignment, [words[0]]), words[-1]
    elif len(words) == 4:
        return Command(bitwise_not, [words[1]]), words[-1]
    inputs = [words[0], words[2]]
    match words[1]:
        case "AND":
            return Command(bitwise_and, inputs), words[-1]
        case "OR":
            return Command(bitwise_or, inputs), words[-1]
        case "LSHIFT":
            return Command(bitwise_lshift, inputs), words[-1]
        case "RSHIFT":
            return Command(bitwise_rshift, inputs), words[-1]
        case _:
            print('Invalid instruction')
    raise Exception("Invalid instruction")


main()
