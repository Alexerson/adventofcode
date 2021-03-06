from intcode import Program

from utils import data_import


def part1(data):
    return Program(data).run_until_output([1])


def part2(data):
    return Program(data).run_until_output([2])


if __name__ == '__main__':

    data = data_import('y2019/data/day9', cast=int, split_char=',')[0]

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
