import collections

from src.utils import data_import


def part1(list1: list[int], list2: list[int]) -> int:
    list1 = sorted(list1)
    list2 = sorted(list2)

    return sum(abs(a - b) for a, b in zip(list1, list2))


def part2(list1: list[int], list2: list[int]) -> int:
    list2_counts = collections.Counter(list2)
    return sum(a * list2_counts.get(a, 0) for a in list1)


if __name__ == '__main__':
    mydata = data_import('data/y2024/day1', int, split_char=' ')

    list1: list[int] = []
    list2: list[int] = []
    for a, b in mydata:
        list1.append(a)
        list2.append(b)

    # print('Input is', mydata)
    print('Solution of 1 is', part1(list1, list2))
    print('Solution of 2 is', part2(list1, list2))
