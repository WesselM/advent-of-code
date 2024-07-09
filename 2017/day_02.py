# https://adventofcode.com/2017/day/2

def main():
    with open("2017/examples/ex_02.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 18
    assert part_two(ex) == 9

    with open("2017/input/inp_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(spreadsheet: list[str]):
    spreadsheet = list(map(lambda row: list(map(int, row.split())),
                           spreadsheet))

    return sum([max(row) - min(row) for row in spreadsheet])


def part_two(spreadsheet: list[str]):
    spreadsheet = list(map(lambda row: list(map(int, row.split())),
                           spreadsheet))
    pairs = list(map(lambda row: [sorted((row[i], row[j]), reverse=True)
                                  for i in range(len(spreadsheet))
                                  for j in range(i + 1, len(row))],
                     spreadsheet))

    return sum([a // b for row in pairs for a, b in row
                if a != b and a % b == 0])


if __name__ == '__main__':
    main()
