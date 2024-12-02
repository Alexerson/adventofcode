from src.utils import data_import

from .intcode import Program


def part1(data):
    return Program(data).run_until_output([1])


def part2(data):
    return Program(data).run_until_output([2])


if __name__ == '__main__':
    data = data_import('data/y2019/day9', cast=int, split_char=',')[0]

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
