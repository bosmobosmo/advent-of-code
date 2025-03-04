def find_possible_triangles(triangles: list[list[int]]) -> int:
    possible = 0
    for sides in triangles:
        longest_side = max(sides)
        possible += (sum(sides) - longest_side) > longest_side
    return possible


if __name__ == "__main__":
    with open("input") as f:
        part_one_triangles: list[list[int]] = []
        part_two_triangles: list[list[int]] = []
        triangle_one: list[int] = []
        triangle_two: list[int] = []
        triangle_three: list[int] = []
        row = 1
        for line in f.readlines():
            numbers: list[int] = [eval(num) for num in line.strip().split()]
            part_one_triangles.append(numbers)
            triangle_one.append(numbers[0])
            triangle_two.append(numbers[1])
            triangle_three.append(numbers[2])
            if row % 3 == 0:
                part_two_triangles.extend(
                    [triangle_one, triangle_two, triangle_three]
                )
                triangle_one = []
                triangle_two = []
                triangle_three = []
            row += 1

    print(f"Part one answer is {find_possible_triangles(part_one_triangles)}")
    print(f"Part two answer is {find_possible_triangles(part_two_triangles)}")
