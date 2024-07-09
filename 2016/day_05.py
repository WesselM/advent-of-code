# https://adventofcode.com/2016/day/5


import hashlib


def main():
    with open("2016/examples/ex_05.txt", "r") as f:
        ex = f.read().strip()

    assert part_one(ex) == "18f47a30"
    assert part_two(ex) == "05ace8e3"

    with open("2016/input/inp_05.txt", "r") as f:
        inp = f.read().strip()

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(door_id):
    password = ""
    for i in range(int(1E10)):
        hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith("0" * 5):
            password += hash[5]
        if len(password) >= 8:
            break

    return password


def part_two(door_id):
    password = ["#" for _ in range(8)]
    for i in range(int(1E10)):
        hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith("0" * 5) and hash[5].isdigit():
            index = int(hash[5])
            if index < len(password) and password[index] == "#":
                password[index] = hash[6]

        if "#" not in password:
            break

    return "".join(password)


if __name__ == '__main__':
    main()
