# https://adventofcode.com/2019/day/4

def main():
    with open("2019/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    # assert part_one(ex) == 1
    # assert part_two(ex) == 1

    # with open("2019/input/inp_04.txt", "r") as f:
    #     inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(ex))
    # print("Part two:", part_two(inp))


def part_one(entries):
    return entries[0]


def part_two(entries):
    return entries[0]


if __name__ == '__main__':
    main()
