# https://adventofcode.com/2022/day/5

def main():
    with open("2022/examples/ex_05.txt", "r") as f:
        ex = list(map(str, f.read().split("\n")))

    assert part_one(ex) == "CMZ"
    assert part_two(ex) == "MCD"

    with open("2022/input/inp_05.txt", "r") as f:
        inp = list(map(str, f.read().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(procedure):
    starting_stacks = procedure[:procedure.index('')]
    rearrangements = procedure[procedure.index('') + 1:]
    n_stacks = int(starting_stacks.pop().split()[-1])

    stacks = [[] * n for n in range(n_stacks)]
    for row in reversed(starting_stacks):
        for index, value in enumerate(list(row)[1:-1:4]):
            if value != " ":
                stacks[index].append(value)

    for rearrangement in rearrangements:
        _, n, _, src, _, dst = rearrangement.split()
        n, src, dst = int(n), int(src) - 1, int(dst) - 1
        for _ in range(n):
            stacks[dst].append(stacks[src].pop())

    return ''.join(stack[-1] for stack in stacks)


def part_two(procedure):
    starting_stacks = procedure[:procedure.index('')]
    rearrangements = procedure[procedure.index('') + 1:]
    n_stacks = int(starting_stacks.pop().split()[-1])

    stacks = [[] * n for n in range(n_stacks)]
    for row in reversed(starting_stacks):
        for index, value in enumerate(list(row)[1:-1:4]):
            if value != " ":
                stacks[index].append(value)

    for rearrangement in rearrangements:
        _, n, _, src, _, dst = rearrangement.split()
        n, src, dst = int(n), int(src) - 1, int(dst) - 1
        stacks[dst].extend(stacks[src][-n:])
        stacks[src] = stacks[src][:-n]

    return ''.join(stack[-1] for stack in stacks)


if __name__ == '__main__':
    main()
