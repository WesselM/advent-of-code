# https://adventofcode.com/2022/day/4

def main():
    with open("2022/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 2
    assert part_two(ex) == 4

    with open("2022/input/inp_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(section_assignments):
    containments = 0
    for assignment in section_assignments:
        left, right = assignment.split(",")
        left_start, left_end = map(int, left.split("-"))
        right_start, right_end = map(int, right.split("-"))
        if left_start >= right_start and left_end <= right_end or \
                right_start >= left_start and right_end <= left_end:
            containments += 1

    return containments


def part_two(section_assignments):
    overlaps = 0
    for assignment in section_assignments:
        left, right = assignment.split(",")
        left_start, left_end = map(int, left.split("-"))
        right_start, right_end = map(int, right.split("-"))
        if not (left_end < right_start or right_end < left_start):
            overlaps += 1

    return overlaps


if __name__ == '__main__':
    main()
