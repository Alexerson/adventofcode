import re

from src.utils import data_import


def part1(data: str) -> int:
    regexp = re.compile(r'mul\((\d+),(\d+)\)')

    return sum(int(a) * int(b) for a, b in regexp.findall(data))  # type: ignore[misc]


def part2(data: str) -> int:
    data = f"do(){data}don't()"
    # find all the valid bits (between "do()" and "don't()")
    regexp_valid = re.compile(r"do\(\)(.*?)don't\(\)")

    return sum(part1(valid) for valid in regexp_valid.findall(data))  # type: ignore[misc]


if __name__ == '__main__':
    mydata = data_import('data/y2024/day3-example')[0]
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))

    # The real data has multiple lines, so we need to join them
    mydata = ' '.join(data_import('data/y2024/day3'))
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
