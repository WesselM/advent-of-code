# https://adventofcode.com/2021/day/3

def main():
    with open("2021/examples/ex_03.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 198
    assert part_two(ex) == 230

    with open("2021/input/inp_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(diagnostics):
    transposed = transpose(diagnostics)
    gamma = "".join(max(bits, key=bits.count) for bits in transposed)
    epsilon = "".join("0" if b == "1" else "1" for b in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def part_two(diagnostics):
    oxygen = get_rating(diagnostics, "most")
    co2 = get_rating(diagnostics, "least")
    return oxygen * co2


def get_rating(diagnostics, criteria):
    candidates = diagnostics[:]
    for i in range(len(diagnostics[0])):
        if len(candidates) == 1:
            break
        column = [num[i] for num in candidates]
        ones = column.count("1")
        zeros = len(column) - ones
        if criteria == "most":
            desired_bit = "1" if ones >= zeros else "0"
        else:  # criteria == "least"
            desired_bit = "0" if zeros <= ones else "1"
        candidates = [num for num in candidates if num[i] == desired_bit]
    return int(candidates[0], 2)


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


if __name__ == '__main__':
    main()
