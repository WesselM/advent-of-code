# https://adventofcode.com/2018/day/2

from functools import reduce
from operator import mul
from string import ascii_lowercase


def main():
    with open("2018/examples/ex_02.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 12
    assert part_two(ex) == "abcde"

    with open("2018/input/inp_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(ids: list[str]):
    return reduce(mul, [sum(counts) for counts in zip(*[
        (any([id.count(letter) == 2 for letter in ascii_lowercase]),
         any([id.count(letter) == 3 for letter in ascii_lowercase]))
        for id in ids
    ])])


def part_two(ids: list[str]):
    for id1 in ids:
        for id2 in ids:
            overlap = "".join([a for a, b in zip(id1, id2) if a == b])
            if len(overlap) == len(id1) - 1:
                return overlap


if __name__ == '__main__':
    main()
