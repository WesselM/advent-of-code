# https://adventofcode.com/2015/day/2

def main():
    with open("2015/examples/ex_02.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 58
    assert part_two(ex) == 34

    with open("2015/input/inp_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(dimensions):
    total_sqft = 0
    for dimension in dimensions:
        dims = list(map(int, dimension.split("x")))
        pairs = sorted([dims[i] * dims[j] for i in range(len(dims))
                        for j in range(i + 1, len(dims))])
        total_sqft += sum(map(lambda area: area * 2, pairs)) + pairs[0]

    return total_sqft


def part_two(dimensions):
    total_ft = 0
    for dimension in dimensions:
        dims = sorted(list(map(int, dimension.split("x"))))
        total_ft += dims[0] * 2 + dims[1] * 2 + dims[0] * dims[1] * dims[2]

    return total_ft


def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
        return result


if __name__ == '__main__':
    main()
