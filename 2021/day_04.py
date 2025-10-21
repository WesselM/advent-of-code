# https://adventofcode.com/2021/day/4

from collections import defaultdict


def main():
    with open("2021/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n\n")))

    # assert part_one(ex) == 1
    # assert part_two(ex) == 1

    with open("2021/input/inp_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(subsystem):
    draws = list(map(int, subsystem[0].split(",")))
    boards = list(map(lambda b:
                      [list(map(int, line.split())) for line in b.split("\n")],
                      subsystem[1:]))

    pos = defaultdict(list)
    n_boards = len(boards)
    size = len(boards[0])
    unmarked = [0]*n_boards
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, num in enumerate(row):
                pos[num].append((b, r, c))
                unmarked[b] += num

    row_counts = [[0]*size for _ in range(n_boards)]
    col_counts = [[0]*size for _ in range(n_boards)]
    marked = set()

    for number in draws:
        for b, r, c in pos.get(number, []):
            if (b, r, c) in marked:
                continue
            marked.add((b, r, c))
            row_counts[b][r] += 1
            col_counts[b][c] += 1
            unmarked[b] -= number
            if row_counts[b][r] == size or col_counts[b][c] == size:
                return unmarked[b] * number

    return None


def part_two(subsystem):
    draws = list(map(int, subsystem[0].split(",")))
    boards = list(map(lambda b:
                      [list(map(int, line.split())) for line in b.split("\n")],
                      subsystem[1:]))

    pos = defaultdict(list)
    n_boards = len(boards)
    size = len(boards[0])
    unmarked = [0]*n_boards
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, num in enumerate(row):
                pos[num].append((b, r, c))
                unmarked[b] += num

    row_counts = [[0]*size for _ in range(n_boards)]
    col_counts = [[0]*size for _ in range(n_boards)]
    marked = set()
    won = set()

    last_score = None
    for number in draws:
        for b, r, c in pos.get(number, []):
            if (b, r, c) in marked or b in won:
                continue
            marked.add((b, r, c))
            row_counts[b][r] += 1
            col_counts[b][c] += 1
            unmarked[b] -= number
            if row_counts[b][r] == size or col_counts[b][c] == size:
                won.add(b)
                last_score = unmarked[b] * number

    return last_score


if __name__ == '__main__':
    main()
