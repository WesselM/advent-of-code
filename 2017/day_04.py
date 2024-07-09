# https://adventofcode.com/2017/day/4

def main():
    with open("2017/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 7
    assert part_two(ex) == 5

    with open("2017/input/inp_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(passphrases: list[str]):
    passphrases = list(map(lambda passphrase: passphrase.split(), passphrases))
    return sum([len(passphrase) == len(set(passphrase))
               for passphrase in passphrases])


def part_two(passphrases):
    passphrases = list(map(lambda passphrase: ["".join(sorted(word))
                                               for word in passphrase.split()],
                           passphrases))

    return sum([len(passphrase) == len(set(passphrase))
               for passphrase in passphrases])


if __name__ == '__main__':
    main()
