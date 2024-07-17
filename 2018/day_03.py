# https://adventofcode.com/2018/day/3

import re


def main():
    with open("2018/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 4
    assert part_two(ex) == 3

    with open("2018/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(claims: list[str]):
    fabric = [[set() for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        id, d_left, d_top, width, height = \
            map(int,
                re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim).groups())
        for y in range(d_top, d_top + height):
            for x in range(d_left, d_left + width):
                fabric[y][x].add(id)

    return sum(len(ids) >= 2 for row in fabric for ids in row)


def part_two(claims: list[str]):
    fabric = [[set() for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        id, d_left, d_top, width, height = \
            map(int,
                re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim).groups())
        for y in range(d_top, d_top + height):
            for x in range(d_left, d_left + width):
                fabric[y][x].add(id)

    for i in range(1, id + 1):
        if all(len(ids) == 1 for row in fabric for ids in row if i in ids):
            return i


if __name__ == '__main__':
    main()
