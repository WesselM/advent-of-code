# https://adventofcode.com/2015/day/5

def main():
    with open("2015/examples/ex_05.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 2
    assert part_two(ex) == 2

    with open("2015/input/inp_05.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(strings: list[str]):
    vowels = list("aeiou")
    invalid_strings = ["ab", "cd", "pq", "xy"]
    n_nice_strings = 0

    for string in strings:
        if sum([string.count(vowel) for vowel in vowels]) >= 3 and \
                any(a == b for a, b in zip(string, string[1:])) and \
                not any([invalid in string for invalid in invalid_strings]):
            n_nice_strings += 1

    return n_nice_strings


def part_two(strings: list[str]):
    n_nice_strings = 0
    for string in strings:
        p1 = p2 = False
        for i in range(len(string) - 1):
            if string[i:i+2] in string[i+2:]:
                p1 = True
                break

        for i in range(len(string) - 2):
            if string[i] == string[i+2]:
                p2 = True
                break

        if p1 and p2:
            n_nice_strings += 1

    return n_nice_strings


if __name__ == '__main__':
    main()
