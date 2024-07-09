# https://adventofcode.com/2016/day/4

from string import ascii_lowercase


def main():
    with open("2016/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split()))

    assert part_one(ex) == 1514
    # assert part_two(ex) == 1

    with open("2016/input/inp_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(rooms: list[str]):
    sum_sector_ids = 0
    for room in rooms:
        room = room[:-1].split("-")
        name = "".join(room[:-1])
        sector_id, checksum = room[-1].split("[")
        most_common = "".join([letter for letter, _ in
                               sorted([(letter, name.count(letter))
                                       for letter in ascii_lowercase],
                                      key=lambda x: x[1],
                                      reverse=True)[:5]])

        if checksum == most_common:
            sum_sector_ids += int(sector_id)

    return sum_sector_ids


def part_two(rooms: list[str]):
    for room in rooms:
        room = room[:-1].split("-")
        name = " ".join(room[:-1])
        sector_id = room[-1].split("[")[0]
        name = "".join(
            [chr(((ord(char) - ord('a') + int(sector_id)) % 26) + ord('a'))
             if char in ascii_lowercase else char for char in name])

        if "north" in name:
            return sector_id


if __name__ == '__main__':
    main()
