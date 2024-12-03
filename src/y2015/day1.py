import collections

from src.utils import data_import


def part1(mydata: str) -> int:
    counter = collections.Counter(mydata)
    return counter['('] - counter[')']


def part2(mydata: str) -> int:
    current_level = 0
    for index, char in enumerate(mydata):
        current_level += 1 if char == '(' else -1

        if current_level == -1:
            return index + 1
    return 0


if __name__ == '__main__':
    mydata = data_import('data/y2015/day1')[0]

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
