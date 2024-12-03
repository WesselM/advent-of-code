# https://adventofcode.com/2020/day/2

def main():
    with open("2020/examples/ex_02.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 2
    assert part_two(ex) == 1

    with open("2020/input/inp_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(passwords: list[str]):
    valid_passwords = 0
    for password in passwords:
        bounds, letter, pwd = password.split(" ")
        lower, upper = map(int, bounds.split("-"))
        letter = letter[:-1]
        count = pwd.count(letter)

        if (lower <= count and count <= upper):
            valid_passwords += 1

    return valid_passwords


def part_two(passwords: list[str]):
    valid_passwords = 0
    for password in passwords:
        positions, letter, pwd = password.split(" ")
        left, right = map(int, positions.split("-"))
        letter = letter[:-1]

        if (pwd[left-1] == letter) ^ (pwd[right-1] == letter):
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    main()
