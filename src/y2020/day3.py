import math
from typing import List

from adventofcode.utils import data_import


def is_tree(nrow, ncol, data) -> bool:
    row = data[nrow]
    return row[ncol % len(row)] == '#'


def part1(data: List[str], move=(1, 3)) -> int:
    nrows = len(data)
    trees = 0
    position = (0, 0)
    while position[0] < nrows:
        trees += is_tree(position[0], position[1], data)
        position = (position[0] + move[0], position[1] + move[1])

    return trees


def part2(data: List[str]) -> int:
    moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return math.prod(part1(data, move) for move in moves)


if __name__ == '__main__':
    mydata = data_import('data/y2020/day3')
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
