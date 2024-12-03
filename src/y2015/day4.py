from hashlib import md5
from itertools import count

from src.utils import data_import


def part1(mydata: str) -> int:
    for padding in count():
        if md5(f'{mydata}{padding}'.encode()).hexdigest().startswith('00000'):
            return padding
    return -1


def part2(mydata: str) -> int:
    for padding in count():
        if md5(f'{mydata}{padding}'.encode()).hexdigest().startswith('000000'):
            return padding
    return -1


if __name__ == '__main__':
    mydata = data_import('data/y2015/day4')[0]

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
