# https://adventofcode.com/2018/day/5

def main():
    with open("2018/examples/ex_05.txt", "r") as f:
        ex = f.read().strip()

    assert part_one(ex) == 10
    assert part_two(ex) == 4

    with open("2018/input/inp_05.txt", "r") as f:
        inp = f.read().strip()

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def react(polymer):
    remaining = []
    for unit in polymer:
        if remaining and unit == remaining[-1].swapcase():
            remaining.pop()
        else:
            remaining.append(unit)
    return remaining


def part_one(polymer: str):
    return len(react(polymer))


def part_two(polymer: str):
    return min(len(react(polymer.replace(c, "").replace(c.upper(), "")))
               for c in set(polymer.lower()))


if __name__ == '__main__':
    main()
