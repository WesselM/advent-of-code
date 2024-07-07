# https://adventofcode.com/2023/day/5

def main():
    with open("2023/examples/ex_05.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    # assert part_one(ex) == 1
    # assert part_two(ex) == 1

    # with open("2023/input/inp_05.txt", "r") as f:
    #     inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(ex))
    # print("Part two:", part_two(inp))


def part_one(entries):
    return entries[0]


def part_two(entries):
    return entries[0]


if __name__ == '__main__':
    main()
