from collections import deque
from itertools import combinations
from typing import List

from utils import data_import


class NoSolutionError(Exception):
    pass


def part1(data: List[int], length: int = 25) -> int:
    considered_set = deque(data[:length])

    for number in data[length:]:
        possible_sums = {a + b for a, b in combinations(considered_set, 2)}
        if number not in possible_sums:
            return number

        considered_set.append(number)
        considered_set.popleft()

    raise NoSolutionError


def part2(data: List[int], target: int) -> int:
    for i, value in enumerate(data):
        current_sum = value
        min_value = value
        max_value = value
        for value2 in data[i + 1 :]:
            current_sum += value2
            max_value = max(value2, max_value)
            min_value = min(value2, min_value)
            if current_sum == target:
                return min_value + max_value

    raise NoSolutionError


if __name__ == '__main__':
    mydata = data_import('data/y2020/day9', cast=int)
    print('Input is', mydata[:10])
    print('Input length is', len(mydata))

    print('Solution of 1 is', solution1 := part1(mydata))
    print('Solution of 2 is', part2(mydata, target=solution1))
