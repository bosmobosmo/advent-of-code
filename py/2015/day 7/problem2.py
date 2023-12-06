from __future__ import annotations
from copy import deepcopy

from common import (
    Circuit
)


def main() -> None:
    circuit = Circuit()
    with open('input.txt') as f:
        for instruction in f.read().splitlines():
            circuit.build_circuit(instruction)
    # create copy of circuit
    circuit_copy = deepcopy(circuit.circuit)
    # calling get_output triggers memoization
    a = circuit.get_output('a')
    circuit.circuit = circuit_copy
    # send result of a to b
    circuit.build_circuit(f'{a} -> b')
    print(circuit.get_output('a'))


main()
