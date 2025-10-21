# https://adventofcode.com/2022/day/2


def main():
    with open("2022/examples/ex_02.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 15
    assert part_two(ex) == 12

    with open("2022/input/inp_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(strategy_guide):
    YOU = {'X': 1, 'Y': 2, 'Z': 3}
    OPP = {'A': 1, 'B': 2, 'C': 3}
    RES = {0: 3, 1: 6, 2: 0}
    return sum(RES[(YOU[y]-OPP[o]) % 3] + YOU[y]
               for o, y in (line.split() for line in strategy_guide))


def part_two(strategy_guide):
    YOU = {'X': 0, 'Y': 3, 'Z': 6}
    OPP = {'A': 1, 'B': 2, 'C': 3}
    MOVE = {0: 3, 1: 1, 2: 2}
    return sum(YOU[y] + MOVE[(OPP[o] + (YOU[y] // 3 - 1)) % 3]
               for o, y in (line.split() for line in strategy_guide))


if __name__ == '__main__':
    main()
