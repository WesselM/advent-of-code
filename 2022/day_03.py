# https://adventofcode.com/2022/day/3

def main():
    with open("2022/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 157
    assert part_two(ex) == 70

    with open("2022/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(rucksacks):
    sum_priorities = 0
    for rucksack in rucksacks:
        first = set(rucksack[:len(rucksack) // 2])
        second = set(rucksack[len(rucksack) // 2:])
        overlap = ord(next(iter(first & second)))
        sum_priorities += overlap - 96 if overlap > 90 else overlap - 38

    return sum_priorities


def part_two(rucksacks):
    sum_priorities = 0
    for a, b, c in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]):
        badge = ord(next(iter(set(a) & set(b) & set(c))))
        sum_priorities += badge - 96 if badge > 90 else badge - 38

    return sum_priorities


if __name__ == "__main__":
    main()
