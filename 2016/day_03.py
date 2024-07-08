# https://adventofcode.com/2016/day/3

from itertools import starmap


def main():
    with open("2016/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 3
    assert part_two(ex) == 6

    with open("2016/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(triangles: list[str]):
    triangles = list(map(lambda triangle:
                         tuple(map(int, triangle.split())), triangles))

    return sum(list(starmap(
        lambda a, b, c: a + b > c and a + c > b and b + c > a,
        triangles)))


def part_two(triangles: list[str]):
    triangles = list(map(lambda triangle:
                         list(map(int, triangle.split())), triangles))

    triangles = [combination for combinations in [list(zip(*triangles[i:i+3]))
                 for i in range(0, len(triangles) - 2, 3)]
                 for combination in combinations]

    return sum(list(starmap(
        lambda a, b, c: a + b > c and a + c > b and b + c > a,
        triangles)))


if __name__ == '__main__':
    main()
