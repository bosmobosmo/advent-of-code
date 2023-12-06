# from abc import ABC, abstractmethod
from typing import Callable, Generic, NamedTuple, TypedDict, TypeVar

T = TypeVar('T')


operator = Callable[[T], T]


class Operators(TypedDict):
    toggle: operator
    turn_off: operator
    turn_on: operator


class InstructionMap(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int


def parse_command(input: str) -> tuple[str, InstructionMap]:
    command = input.lower().split(' ')
    if 'turn' in command:
        command.remove('turn')
    command.remove('through')
    instruction = command[0]
    x1, y1 = command[1].split(',')
    x2, y2 = command[2].split(',')
    return instruction, InstructionMap(int(x1), int(y1), int(x2), int(y2))


class Operator(Generic[T]):

    def __init__(
        self, grid: list[list[T]],
        operators: Operators
    ) -> None:
        self.grid = grid
        self.toggle = operators['toggle']
        self.turn_on = operators['turn_on']
        self.turn_off = operators['turn_off']

    def run_instruction(
        self, instruction: str, map: InstructionMap
    ) -> None:
        match instruction:
            case 'toggle':
                operation = self.toggle
            case 'on':
                operation = self.turn_on
            case 'off':
                operation = self.turn_off
            case _:
                raise NotImplementedError()
        for x in range(map.x1, map.x2 + 1):
            for y in range(map.y1, map.y2 + 1):
                self.grid[x][y] = operation(self.grid[x][y])
