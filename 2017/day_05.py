# https://adventofcode.com/2017/day/5

def main():
    with open("2017/examples/ex_05.txt", "r") as f:
        ex = list(map(int, f.read().strip().split()))

    assert part_one(ex) == 5
    assert part_two(ex) == 10

    with open("2017/input/inp_05.txt", "r") as f:
        inp = list(map(int, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(instructions: list[int]):
    index = counter = 0
    instructions = instructions.copy()
    while index < len(instructions):
        offset = index + instructions[index]
        instructions[index] += 1
        index = offset
        counter += 1

    return counter


def part_two(instructions: list[int]):
    index = counter = 0
    while index < len(instructions):
        offset = index + instructions[index]
        instructions[index] += -1 if instructions[index] >= 3 else 1
        index = offset
        counter += 1

    return counter


if __name__ == '__main__':
    main()
