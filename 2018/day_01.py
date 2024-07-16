# https://adventofcode.com/2018/day/1

def main():
    with open("2018/examples/ex_01.txt", "r") as f:
        ex = list(map(int, f.read().strip().split()))

    assert part_one(ex) == 3
    assert part_two(ex) == 2

    with open("2018/input/inp_01.txt", "r") as f:
        inp = list(map(int, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(frequency_changes):
    return sum(frequency_changes)


def part_two(frequency_changes):
    index = current = 0
    reached = set()
    while (True):
        current += frequency_changes[index]
        index = (index + 1) % len(frequency_changes)
        if current in reached:
            return current
        else:
            reached.add(current)


if __name__ == '__main__':
    main()
