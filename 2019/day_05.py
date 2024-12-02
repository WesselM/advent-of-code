# https://adventofcode.com/2019/day/5

def main():
    with open("2019/examples/ex_05.txt", "r") as f:
        ex = list(map(int, f.read().strip().split(",")))

    assert part_one(ex) == 1
    assert part_two(ex) == 5

    with open("2019/input/inp_05.txt", "r") as f:
        inp = list(map(int, f.read().strip().split(",")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(diagnostic_program: list):
    return intcode_computer(diagnostic_program, 1)


def part_two(diagnostic_program: list):
    return intcode_computer(diagnostic_program, 5)


def intcode_computer(intcode_program, input):
    program = intcode_program.copy()
    output = "No result"
    ip = 0  # instruction pointer

    while True:
        opcode = program[ip] % 100
        mode1 = (program[ip] // 100) % 10
        mode2 = (program[ip] // 1000) % 10
        # mode3 = (program[ip] // 10000) % 10

        if opcode == 99:
            break

        param1 = program[ip+1] if mode1 == 1 else program[program[ip+1]]

        if opcode in [1, 2, 5, 6, 7, 8]:
            param2 = program[ip+2] if mode2 == 1 else program[program[ip+2]]
            param3 = program[ip + 3]

        match opcode:
            case 1:
                program[param3] = param1 + param2
                ip += 4
            case 2:
                program[param3] = param1 * param2
                ip += 4
            case 3:
                program[program[ip + 1]] = input
                ip += 2
            case 4:
                output = param1
                ip += 2
            case 5:
                ip = param2 if param1 != 0 else ip + 3
            case 6:
                ip = param2 if param1 == 0 else ip + 3
            case 7:
                program[param3] = 1 if param1 < param2 else 0
                ip += 4
            case 8:
                program[param3] = 1 if param1 == param2 else 0
                ip += 4
            case _:
                output = f"Unknown opcode {opcode}"
                break

    return output


if __name__ == '__main__':
    main()
