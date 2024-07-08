# https://adventofcode.com/2015/day/3

from collections import defaultdict


def main():
    with open("2015/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip()))

    assert part_one(ex) == 4
    assert part_two(ex) == 3

    with open("2015/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(directions):
    x = y = 0
    visited = defaultdict(int)
    visited[(0, 0)] = 1

    for direction in directions:
        match direction:
            case "^":
                y += 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "<":
                x -= 1

        visited[(x, y)] += 1

    return len(visited)


def part_two(directions):
    coords = [[0, 0], [0, 0]]
    turn = False
    visited = defaultdict(int)
    for direction in directions:
        match direction:
            case "^":
                coords[turn][1] += 1
            case ">":
                coords[turn][0] += 1
            case "v":
                coords[turn][1] -= 1
            case "<":
                coords[turn][0] -= 1

        visited[(coords[turn][0], coords[turn][1])] += 1

        turn = not turn

    return len(visited)


if __name__ == '__main__':
    main()
