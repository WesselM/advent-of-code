# https://adventofcode.com/2018/day/4

from collections import defaultdict
from datetime import datetime
import re


def main():
    with open("2018/examples/ex_04.txt", "r") as f:
        ex = list(map(str, f.read().strip().split("\n")))

    assert part_one(ex) == 240
    assert part_two(ex) == 4455

    with open("2018/input/inp_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def get_timestamp(record: str):
    return datetime.strptime(record.split("]")[0], "[%Y-%m-%d %H:%M")


def part_one(records: list[str]):
    minutes = defaultdict(lambda: defaultdict(int))
    for record in sorted(records):
        if "Guard" in record:
            guard = int(re.search(r'#(\d+)', record).group(1))
        elif "asleep" in record:
            asleep = int(re.search(r':(\d+)', record).group(1))
        elif "wakes" in record:
            for minute in range(asleep,
                                int(re.search(r':(\d+)', record).group(1))):
                minutes[guard][minute] += 1

    guard = max(minutes.items(), key=lambda x: sum(x[1].values()))[0]
    minute = max(minutes[guard].items(), key=lambda x: x[1])[0]

    return guard * minute


def part_two(records: list[str]):
    minutes = defaultdict(lambda: defaultdict(int))
    for record in sorted(records):
        if "Guard" in record:
            guard = int(re.search(r'#(\d+)', record).group(1))
        elif "asleep" in record:
            asleep = int(re.search(r':(\d+)', record).group(1))
        elif "wakes" in record:
            for minute in range(asleep,
                                int(re.search(r':(\d+)', record).group(1))):
                minutes[guard][minute] += 1

    freq = max(minutes.items(), key=lambda x: max(x[1].values()))
    guard = freq[0]
    minute = max(freq[1].items(), key=lambda x: x[1])[0]

    return guard * minute


if __name__ == '__main__':
    main()
