from math import inf

# VERY BADLY OPTIMIZED
def main(compartment_count: int) -> int:
    with open("input") as f:
        packages = [int(line.strip()) for line in f.readlines()]
    packages.reverse()
    weight_per_group = sum(packages) / compartment_count
    group_arrangements = []  # package arrangements for a group

    def _can_fit(index: int, arrangement: list[int]) -> None:
        package = packages[index]
        if package in arrangement:
            return
        arrangement.append(package)
        space_left = weight_per_group - sum(arrangement)
        if space_left < 0:
            arrangement.pop()
            return
        if space_left == 0:
            group_arrangements.append(arrangement)
            return
        for i in range(index + 1, len(packages)):
            _can_fit(i, arrangement.copy())

    for i in range(len(packages)):
        _can_fit(i, [])
    group_arrangements.sort(key=lambda x: len(x))
    most_legroom = len(group_arrangements[0])
    smallest_groups = [
        group for group in group_arrangements if len(group) == most_legroom
    ]

    smallest_group = []
    smallest_number = inf
    for group in smallest_groups:
        quantum_number = 1
        for package in group:
            quantum_number *= package
        if quantum_number <= smallest_number:
            smallest_number = quantum_number
            smallest_group = group
    print(f"Smallest group is {smallest_group}")
    return smallest_number


if __name__ == "__main__":
    # print(f"The answer to part one is {main(3)}")
    print(f"The answer to part two is {main(4)}")
