# https://adventofcode.com/2016/day/3

from itertools import starmap


def main():
    with open("2016/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 1
    # assert part_two(ex) == 1

    with open("2016/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    # print("Part two:", part_two(ex))


def part_one(triangles: list[str]):
    triangles = list(map(lambda triangle:
                         tuple(map(int, triangle.split())), triangles))

    return sum(list(starmap(
        lambda a, b, c: a + b > c and a + c > b and b + c > a,
        triangles)))


def part_two(triangles):
    return 0


if __name__ == '__main__':
    main()
