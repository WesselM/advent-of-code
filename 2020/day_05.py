# https://adventofcode.com/2020/day/5

def main():
    with open("2020/examples/ex_05.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 820
    # assert part_two(ex) == None

    with open("2020/input/inp_05.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(boarding_passes: list[str]):
    return max([int(p.replace("B", "1").replace("F", "0")
                    .replace("R", "1").replace("L", "0"), 2)
                for p in boarding_passes])


def part_two(boarding_passes: list[str]):
    taken = {int(p.replace("B", "1").replace("F", "0").replace("R", "1").
                 replace("L", "0"), 2) for p in boarding_passes}
    available = set(range(128 * 8)) - taken

    for seat in available:
        if seat - 1 not in available and seat + 1 not in available:
            return seat


if __name__ == '__main__':
    main()
