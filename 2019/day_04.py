# https://adventofcode.com/2019/day/4

def main():
    with open("2019/examples/ex_04.txt", "r") as f:
        ex = list(map(int, f.read().strip().split("-")))

    assert part_one(ex) == 1
    assert part_two(ex) == 1

    with open("2019/input/inp_04.txt", "r") as f:
        inp = list(map(int, f.read().strip().split("-")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(endpoints):
    valid_passwords = 0

    for password in map(str, range(endpoints[0], endpoints[1])):
        adjacent_digits = False
        never_decreases = True

        for i in range(5):
            if password[i] == password[i+1]:
                adjacent_digits = True

            if password[i] > password[i+1]:
                never_decreases = False
                break

        if adjacent_digits and never_decreases:
            valid_passwords += 1

    return valid_passwords


def part_two(endpoints):
    valid_passwords = 0

    for password in map(str, range(endpoints[0], endpoints[1])):
        adjacent_digits = False
        never_decreases = True

        for i in range(5):
            if password[i] > password[i+1]:
                never_decreases = False
                break

            if password[i] == password[i + 1] and \
                (i == 0 or password[i] != password[i - 1]) and \
                    (i + 1 == 5 or password[i] != password[i + 2]):
                adjacent_digits = True

        if adjacent_digits and never_decreases:
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    main()
