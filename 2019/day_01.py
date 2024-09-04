# https://adventofcode.com/2019/day/1

def main():
    with open("2019/examples/ex_01.txt", "r") as f:
        ex = list(map(int, f.read().strip().split()))

    assert part_one(ex) == 34241
    assert part_two(ex) == 51316

    with open("2019/input/inp_01.txt", "r") as f:
        inp = list(map(int, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(modules):
    return sum(map(lambda mass: mass // 3 - 2, modules))


def part_two(modules):
    return sum(map(additional_fuel, modules))


def additional_fuel(mass):
    fuel = mass // 3 - 2
    return fuel + additional_fuel(fuel) if fuel > 0 else 0


if __name__ == '__main__':
    main()
