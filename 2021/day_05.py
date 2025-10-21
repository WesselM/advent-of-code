# https://adventofcode.com/2021/day/5

def main():
    with open("2021/examples/ex_05.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 5
    assert part_two(ex) == 12

    with open("2021/input/inp_05.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(lines):
    field = [[0]*1000 for _ in range(1000)]
    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = map(int, p1.split(","))
        x2, y2 = map(int, p2.split(","))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[y1][x] += 1

    return sum(1 for row in field for val in row if val > 1)


def part_two(lines):
    field = [[0]*1000 for _ in range(1000)]
    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = map(int, p1.split(","))
        x2, y2 = map(int, p2.split(","))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[y1][x] += 1
        else:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            for d in range(abs(x2 - x1) + 1):
                field[y1 + d * dy][x1 + d * dx] += 1

    return sum(1 for row in field for val in row if val > 1)


if __name__ == '__main__':
    main()
