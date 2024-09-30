# https://adventofcode.com/2019/day/3

from collections import defaultdict


def main():
    with open("2019/examples/ex_03.txt", "r") as f:
        ex = list(map(lambda path: path.split(","),
                  map(str, f.read().strip().split("\n"))))

    assert part_one(ex) == 135
    # assert part_two(ex) == 1

    with open("2019/input/inp_03.txt", "r") as f:
        inp = list(map(lambda path: path.split(","),
                       map(str, f.read().strip().split("\n"))))

    print("Part one:", part_one(inp))
    # print("Part two:", part_two(inp))


def part_one(paths: list[list[int]]):
    directions = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    visited = defaultdict(int)

    for path in paths:
        x = y = 0
        for step in path:
            dx, dy = directions[step[0]]
            dist = int(step[1:])
            for _ in range(dist):
                x += dx
                y += dy
                visited[(x, y)] += 1

    intersects = [(x, y) for (x, y), count in visited.items() if count > 1]

    return min(abs(x) + abs(y) for x, y in intersects) if intersects else None


def part_two(entries):
    return entries[0]


if __name__ == '__main__':
    main()
