# https://adventofcode.com/2023/day/1

import re


def main():
    with open("2023/examples/ex_01.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    # assert part_one(ex) == 142
    assert part_two(ex) == 281

    with open("2023/input/inp_01.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(calibrations):
    total = sum(int(nums[0] + nums[-1])
                for cal in calibrations
                for nums in (re.findall(r'\d', cal),))

    return total


def part_two(calibrations):
    for i in range(len(calibrations)):
        for key, value in WORDS.items():
            calibrations[i] = calibrations[i].replace(key, value)

    total = sum(int(nums[0] + nums[-1])
                for cal in calibrations
                for nums in (re.findall(r'\d', cal),))

    return total


WORDS = {
    'one': 'o1e', 'two': 't2o', 'three': 't3e',
    'four': 'f4r', 'five': 'f5e', 'six': 's6x',
    'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
}


if __name__ == '__main__':
    main()
