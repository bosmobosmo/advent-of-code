from __future__ import annotations

from common import (
    Circuit
)


def main() -> None:
    circuit = Circuit()
    with open('input.txt') as f:
        for instruction in f.read().splitlines():
            circuit.build_circuit(instruction)
    print(circuit.get_output('a'))


main()
