# https://adventofcode.com/2014/day/1

def main():
    with open("__year__/examples/ex_01.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == -1
    assert part_two(ex) == -1

    with open("__year__/input/inp_01.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(entries):
    return entries[0]


def part_two(entries):
    return entries[0]


if __name__ == '__main__':
    main()
