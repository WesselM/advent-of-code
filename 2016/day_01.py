# https://adventofcode.com/2016/day/1


def main():
    with open("2016/examples/ex_01.txt", "r") as f:
        ex = list(map(str, f.read().strip().split(", ")))

    assert part_one(ex) == 8
    assert part_two(ex) == 4

    with open("2016/input/inp_01.txt", "r") as f:
        inp = list(map(str, f.read().strip().split(", ")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(instructions):
    position = (0, 0)
    direction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for instruction in instructions:
        dir = instruction[0]
        distance = int(instruction[1:])
        direction = (direction + (1 if dir == "R" else -1)) % 4
        position = tuple(map(lambda pos, dist: pos + dist * distance,
                             position,
                             directions[direction]))

    return sum(map(abs, position))


def part_two(instructions):
    position = (0, 0)
    direction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    for instruction in instructions:
        dir = instruction[0]
        distance = int(instruction[1:])
        direction = (direction + (1 if dir == "R" else -1)) % 4
        for _ in range(distance):
            position = tuple(sum(coord)
                             for coord in zip(position, directions[direction]))
            if position in visited:
                return sum(map(abs, position))

            visited.add(position)

    return position


if __name__ == '__main__':
    main()
