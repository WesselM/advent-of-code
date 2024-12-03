# https://adventofcode.com/2020/day/3

import math


def main():
    with open("2020/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 7
    assert part_two(ex) == 336

    with open("2020/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(path):
    return tree_encounter(path, 3, 1)


def part_two(path):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(tree_encounter(path, *slope) for slope in slopes)


def tree_encounter(path, right, down):
    trees = 0
    for i in range(0, len(path), down):
        x = right * i // down % len(path[i])
        if path[i][x] == '#':
            trees += 1

    return trees


if __name__ == '__main__':
    main()
