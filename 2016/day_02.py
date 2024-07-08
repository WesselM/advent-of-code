# https://adventofcode.com/2016/day/2

def main():
    with open("2016/examples/ex_02.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == "1985"
    assert part_two(ex) == "5DB3"

    with open("2016/input/inp_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(procedure):
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    x = y = 1
    bathroom_code = ""
    for instructions in procedure:
        for instruction in instructions:
            match instruction:
                case "U":
                    y -= (1 if y > 0 else 0)
                case "D":
                    y += (1 if y < 2 else 0)
                case "L":
                    x -= (1 if x > 0 else 0)
                case "R":
                    x += (1 if x < 2 else 0)

        bathroom_code += str(keypad[y][x])

    return bathroom_code


def part_two(procedure):
    keypad = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0],
              [0, 0, 2, 3, 4, 0, 0],
              [0, 5, 6, 7, 8, 9, 0],
              [0, 0, "A", "B", "C", 0, 0, 0],
              [0, 0, 0, "D", 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],]
    x = 1
    y = 3
    bathroom_code = ""
    for instructions in procedure:
        for instruction in instructions:
            nx, ny = x, y
            match instruction:
                case "U":
                    ny -= 1
                case "D":
                    ny += 1
                case "L":
                    nx -= 1
                case "R":
                    nx += 1

            if keypad[ny][nx] != 0:
                x, y = nx, ny

        bathroom_code += str(keypad[y][x])

    return bathroom_code


if __name__ == '__main__':
    main()
