import collections
from utils import data_import

def part1(list1: list[int], list2: list[int]) -> int:

    list1 = sorted(list1)
    list2 = sorted(list2)

    return sum(abs(a-b) for a, b in zip(list1, list2))


def part2(list1: list[int], list2: list[int]) -> int:
    total = 0
    list2_counts = collections.Counter(list2)
    for a in list1:
        total += a * list2_counts.get(a, 0)
    return total



if __name__ == '__main__':
    mydata = data_import('data/y2024/day1', int,split_char=" ")
    list1, list2 = zip(*mydata)
    list1 = list(list1)
    list2 = list(list2)

    # print('Input is', mydata)
    print('Solution of 1 is', part1(list1, list2))
    print('Solution of 2 is', part2(list1, list2))
