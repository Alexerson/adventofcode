import itertools
import math
from typing import List

from adventofcode.utils import data_import


def part1(data: List[int]) -> int:
    for numbers in itertools.combinations(data, 2):
        if sum(numbers) == 2020:
            return math.prod(numbers)
    msg = 'This input is not solvable'
    raise ValueError(msg)


def part2(data: List[int]) -> int:
    for numbers in itertools.combinations(data, 3):
        if sum(numbers) == 2020:
            return math.prod(numbers)
    msg = 'This input is not solvable'
    raise ValueError(msg)


if __name__ == '__main__':
    mydata = data_import('data/y2020/day1', int)
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
