# https://adventofcode.com/2020/day/1

def main():
    with open("2020/examples/ex_01.txt", "r") as f:
        ex = list(map(int, f.read().strip().split()))

    assert part_one(ex) == 514579
    assert part_two(ex) == 241861950

    with open("2020/input/inp_01.txt", "r") as f:
        inp = list(map(int, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(entries):
    for i, entrie1 in enumerate(entries):
        for entrie2 in entries[i:]:
            if entrie1 + entrie2 == 2020:
                return entrie1 * entrie2


def part_two(entries):
    for i, entrie1 in enumerate(entries):
        for j, entrie2 in enumerate(entries[i:]):
            for entrie3 in entries[j:]:
                if entrie1 + entrie2 + entrie3 == 2020:
                    return entrie1 * entrie2 * entrie3


if __name__ == '__main__':
    main()
