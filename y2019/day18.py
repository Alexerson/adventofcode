import collections
import cProfile
import itertools
import math
import operator
from functools import lru_cache
from time import sleep

from intcode import Program

from utils import data_import


def convert_image(image):
    plan = {}

    for line_no, line in enumerate(image):
        for col_no, pixel in enumerate(line):
            plan[(col_no, line_no)] = pixel
            if pixel == '@':
                origin = (col_no, line_no)

    return plan, origin


def get_accessible_keys(plan, current_position, keys):
    return []


def get_possible_permutations(plan, current_position, done_keys=None):

    keys = {
        pixel: (col_no, line_no) for (col_no, line_no), pixel in plan.items()
    }

    return []


def get_total_distance(plan, origin, permutation):
    return 0


def part1(data):

    plan, origin = convert_image(data)

    possible_permutations = get_possible_permutations(plan, origin)

    best = None
    best_permutation = None

    for permutation in possible_permutations:
        distance = get_total_distance(plan, origin, permutation)
        if best is None or distance < best:
            best = distance
            best_permutation = permutation

    return best, best_permutation


def part2(data):
    pass


if __name__ == '__main__':
    data = data_import('y2019/data/day18')
    data_example = data_import('y2019/data/day18_example')
    print('Solution of example 1 is', part1(data_example))
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
