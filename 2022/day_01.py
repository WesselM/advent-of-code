# https://adventofcode.com/2022/day/1

def main():
    with open("2022/examples/ex_01.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n\n")))

    assert part_one(ex) == 24000
    assert part_two(ex) == 45000

    with open("2022/input/inp_01.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(supplies):
    return max([sum([int(calories) for calories in supply.split("\n")])
                for supply in supplies])


def part_two(supplies):
    return sum(sorted([sum([int(calories) for calories in supply.split("\n")])
                       for supply in supplies])[-3:])


if __name__ == '__main__':
    main()
