# https://adventofcode.com/2020/day/4

import re


def main():
    with open("2020/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n\n")))

    assert part_one(ex) == 2
    assert part_two(ex) == 2

    with open("2020/input/inp_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(passports):
    fields = [
        "byr",  # (Birth Year)
        "iyr",  # (Issue Year)
        "eyr",  # (Expiration Year)
        "hgt",  # (Height)
        "hcl",  # (Hair Color)
        "ecl",  # (Eye Color)
        "pid",  # (Passport ID)
    ]

    return sum([all([field in passport for field in fields])
                for passport in passports])


def part_two(passports):
    fields = {
        # (Birth Year) - four digits; at least 1920 and at most 2002.
        "byr": r"byr:\s*(19[2-9]\d|200[0-2])\b",
        # (Issue Year) - four digits; at least 2010 and at most 2020.
        "iyr": r"iyr:\s*20(1\d|20)\b",
        # (Expiration Year) - four digits; at least 2020 and at most 2030.
        "eyr": r"eyr:\s*20(2\d|30)\b",
        # (Height) - a number followed by either cm or in:
        # "If cm, the number must be at least 150 and at most 193.
        # "If in, the number must be at least 59 and at most 76.
        "hgt": r"hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",
        # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        "hcl": r"hcl:\s*#[0-9a-f]{6}\b",
        # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        "ecl": r"ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b",
        # (Passport ID) - a nine-digit number, including leading zeroes.
        "pid": r"pid:\s*\d{9}\b",
        # "cid", # (Country ID) - ignored, missing or not.
    }

    return sum([all([re.search(fields[key], passport) for key in fields])
                for passport in passports])


if __name__ == '__main__':
    main()
