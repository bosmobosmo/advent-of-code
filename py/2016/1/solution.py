CARDINALS = "NESW"
DIRMAP = {
    "N": [1, 0],
    "E": [0, 1],
    "S": [-1, 0],
    "W": [0, -1]
}


def get_distance() -> int:
    with open("input") as f:
        directions = f.read().split(", ")
    facing = "N"
    pos = [0, 0]
    for direction in directions:
        turn = direction[0]
        distance = int(direction[1:])
        match turn:
            case "L":
                facing = CARDINALS[CARDINALS.index(facing) - 1]
            case "R":
                facing = CARDINALS[(CARDINALS.index(facing) + 1) % 4]
            case _:
                raise Exception("Invalid turn direction")
        pos = [
            pos[0] + DIRMAP[facing][0] * distance,
            pos[1] + DIRMAP[facing][1] * distance
        ]
    return abs(pos[0]) + abs(pos[1])


def get_visited_twice_distance() -> int:
    with open("input") as f:
        directions = f.read().split(", ")
    facing = "N"
    pos = [0, 0]
    visited = [[0, 0]]
    for direction in directions:
        turn = direction[0]
        match turn:
            case "L":
                facing = CARDINALS[CARDINALS.index(facing) - 1]
            case "R":
                facing = CARDINALS[(CARDINALS.index(facing) + 1) % 4]
            case _:
                raise Exception("Invalid turn direction")
        for _ in range(int(direction[1:])):
            pos = [
                pos[0] + DIRMAP[facing][0],
                pos[1] + DIRMAP[facing][1]
            ]
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.append(pos)
    raise Exception("No location found")


if __name__ == "__main__":
    print(f"Part one answer is {get_distance()}")
    print(f"Part two answer is {get_visited_twice_distance()}")
