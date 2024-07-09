# https://adventofcode.com/2017/day/1


def main():
    with open("2017/examples/ex_01.txt", "r") as f:
        ex = list(map(int, f.read().strip()))

    assert part_one(ex) == 2
    assert part_two(ex) == 6

    with open("2017/input/inp_01.txt", "r") as f:
        inp = list(map(int, f.read().strip()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(sequence: list[int]):
    sequence.append(sequence[0])
    return sum([x[0] for x in (filter(lambda x: x[0] == x[1],
                                      list(zip(sequence, sequence[1:]))))])


def part_two(sequence: list[int]):
    return sum([sum(x) for x in
                (filter(lambda x: x[0] == x[1],
                        list(zip(sequence, sequence[len(sequence) // 2:]))))])


if __name__ == '__main__':
    main()
