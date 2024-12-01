import collections
import cProfile
import itertools
import math
import operator
from functools import lru_cache
from time import sleep

from intcode import Program

from utils import data_import


@lru_cache()
def get_pattern(rank, length):
    times = (length // (4 * (rank + 1))) + 1
    return (
        (
            [0] * (rank + 1)
            + [1] * (rank + 1)
            + [0] * (rank + 1)
            + [-1] * (rank + 1)
        )
        * times
    )[1 : length + 1]


def compute_phase(data, PATTERNS):
    input_len = len(data)
    return [
        abs(sum(map(operator.mul, data, PATTERNS[rank]))) % 10
        for rank in range(input_len)
    ]


def part1(data, steps=100):
    input_len = len(data)
    PATTERNS = [get_pattern(rank, input_len) for rank in range(input_len)]
    for i in range(steps):
        data = compute_phase(data, PATTERNS)
    return ''.join(str(a) for a in data[:8])


def part2(data):
    offset = int(''.join(str(a) for a in data[:7]))

    data = (data * 10000)[offset:]
    input_len = len(data)

    for _ in range(100):
        cusum = 0
        out = []
        for index, item in enumerate(data[::-1]):
            cusum += item
            out.append(cusum % 10)
        out.reverse()
        data = out

    return ''.join(str(a) for a in data[:8])


if __name__ == '__main__':
    data = [int(a) for a in data_import('data/y2019/day16')[0]]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
