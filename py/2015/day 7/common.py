from __future__ import annotations
from dataclasses import dataclass

from typing import Callable, Sequence, Union

InputType = Sequence[str]
LogicGate = Callable[[InputType], int]


@dataclass
class Command:
    gate: LogicGate
    inputs: InputType


class Circuit:
    def __init__(self) -> None:
        self.circuit: dict[str, Union[Command, int]] = {}

    def bitwise_and(self, inputs: InputType) -> int:
        this_input = [
            int(input)
            if input.isdigit()
            else self.get_output(input)
            for input in inputs
        ]
        return this_input[0] & this_input[1]

    def bitwise_or(self, inputs: InputType) -> int:
        this_input = [
            int(input)
            if input.isdigit()
            else self.get_output(input)
            for input in inputs
        ]
        return this_input[0] | this_input[1]

    def bitwise_not(self, inputs: InputType) -> int:
        input = self.get_output(inputs[0])
        return ~input

    def bitwise_lshift(self, inputs: InputType) -> int:
        steps = int(inputs[1])
        input = self.get_output(inputs[0])
        return input << steps

    def bitwise_rshift(self, inputs: InputType) -> int:
        steps = int(inputs[1])
        input = self.get_output(inputs[0])
        return input >> steps

    def direct_assignment(self, inputs: InputType) -> int:
        if inputs[0].isdigit():
            input = int(inputs[0])
        else:
            input = self.get_output(inputs[0])
        return input

    def get_output(self, input: str) -> int:
        stored_value = self.circuit.get(input)
        if stored_value is None:
            raise Exception("Command not found")
        if isinstance(stored_value, int):
            return stored_value
        output = stored_value.gate(stored_value.inputs)
        self.circuit[input] = output
        return output

    def build_circuit(self, instruction: str) -> None:
        words = instruction.split(" ")
        if len(words) == 3:
            self.circuit[words[-1]] = Command(
                self.direct_assignment,
                [words[0]]
            )
            return
        elif len(words) == 4:
            self.circuit[words[-1]] = Command(self.bitwise_not, [words[1]])
            return
        inputs = [words[0], words[2]]
        output = words[-1]
        match words[1]:
            case "AND":
                command = self.bitwise_and
            case "OR":
                command = self.bitwise_or
            case "LSHIFT":
                command = self.bitwise_lshift
            case "RSHIFT":
                command = self.bitwise_rshift
            case _:
                print(instruction)
                raise Exception("Invalid instruction")
        self.circuit[output] = Command(command, inputs)
