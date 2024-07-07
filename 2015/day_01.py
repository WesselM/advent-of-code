# https://adventofcode.com/2015/day/1

def main():
    with open("2015/examples/ex_01.txt", "r") as f:
        ex = list(map(str, f.read().strip()))

    assert part_one(ex) == -1
    assert part_two(ex) == 5

    with open("2015/input/inp_01.txt", "r") as f:
        inp = list(map(str, f.read().strip()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(instructions):
    position = 0
    for instruction in instructions:
        if instruction == "(":
            position += 1
        elif instruction == ")":
            position -= 1

    return position


def part_two(instructions):
    position = 0
    for i, instruction in enumerate(instructions):
        if instruction == "(":
            position += 1
        elif instruction == ")":
            position -= 1

        if position < 0:
            break

    return i + 1


if __name__ == '__main__':
    main()
