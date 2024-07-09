# https://adventofcode.com/2017/day/3

def main():
    with open("2017/examples/ex_03.txt", "r") as f:
        ex = int(f.read().strip())

    assert part_one(ex) == 31
    assert part_two(ex) == 1968

    with open("2017/input/inp_03.txt", "r") as f:
        inp = int(f.read().strip())

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(square):
    steps = direction = passed_sides = col = row = 0
    distance = 1

    for _ in range(1, square):
        match direction:
            case 0: col += 1
            case 1: row -= 1
            case 2: col -= 1
            case 3: row += 1

        steps += 1
        if steps == distance:
            passed_sides += 1
            direction = (direction + 1) % 4
            steps = 0
            if passed_sides % 2 == 0:
                distance += 1

    return abs(col) + abs(row)


def part_two(square):
    grid_size = 100
    grid = [[0] * square for _ in range(grid_size)]
    steps = direction = passed_sides = 0
    col = row = grid_size // 2
    distance = grid[row][col] = 1

    for _ in range(1, grid_size * 2):
        sum_of_adjacent = sum([grid[row + r][col + c]
                               for r in range(-1, 2)
                               for c in range(-1, 2)
                               if 0 <= row + r < len(grid)
                               and 0 <= col + c < len(grid[0])])

        if sum_of_adjacent > square:
            return sum_of_adjacent

        grid[row][col] = sum_of_adjacent

        match direction:
            case 0: col += 1
            case 1: row -= 1
            case 2: col -= 1
            case 3: row += 1

        steps += 1
        if steps == distance:
            passed_sides += 1
            direction = (direction + 1) % 4
            steps = 0
            if passed_sides % 2 == 0:
                distance += 1


if __name__ == '__main__':
    main()
