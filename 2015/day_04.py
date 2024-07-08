# https://adventofcode.com/2015/day/4

import hashlib


def main():
    with open("2015/examples/ex_04.txt", "r") as f:
        ex = f.read().strip()

    assert part_one(ex) == 1048970
    assert part_two(ex) == 5714438

    with open("2015/input/inp_04.txt", "r") as f:
        inp = f.read().strip()

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(key: str):
    for i in range(int(1E10)):
        hash = hashlib.md5((key + str(i)).encode()).hexdigest()
        if hash.startswith("00000"):
            break

    return i


def part_two(key: str):
    for i in range(int(1E10)):
        hash = hashlib.md5((key + str(i)).encode()).hexdigest()
        if hash.startswith("000000"):
            break

    return i


if __name__ == '__main__':
    main()
