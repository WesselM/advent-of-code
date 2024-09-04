# https://adventofcode.com/2019/day/2

def main():
    # with open("2019/examples/ex_02.txt", "r") as f:
    #     ex = list(map(int, f.read().strip().split(",")))

    # assert part_one(ex) == 1
    # assert part_two(ex) == 1

    with open("2019/input/inp_02.txt", "r") as f:
        inp = list(map(int, f.read().strip().split(",")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(intcode):
    intcode[1] = 12
    intcode[2] = 2
    return run_intcode(intcode)


def part_two(intcode):
    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            if run_intcode(intcode) == 19690720:
                return 100 * noun + verb


def run_intcode(intcode):
    intcode = intcode[:]
    for index in range(0, len(intcode), 4):
        a = intcode[intcode[index + 1]]
        b = intcode[intcode[index + 2]]
        match intcode[index]:
            case 99:
                return intcode[0]
            case 1:
                intcode[intcode[index + 3]] = a + b
            case 2:
                intcode[intcode[index + 3]] = a * b

    return intcode


if __name__ == '__main__':
    main()
