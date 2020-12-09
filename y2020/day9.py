from collections import deque
from itertools import combinations
from typing import List

from adventofcode.utils import data_import


def part1(data: List[int], length: int = 25) -> int:
    considered_set = deque(data[:length])

    for number in data[length:]:
        possible_sums = set(a + b for a, b in combinations(considered_set, 2))
        if number not in possible_sums:
            return number

        considered_set.append(number)
        considered_set.popleft()

    raise Exception('No solution')


def part2(data: List[int], target: int) -> int:
    for i, value in enumerate(data):
        current_sum = value
        min_value = value
        max_value = value
        for j, value2 in enumerate(data[i + 1 :]):
            current_sum += value2
            if value2 > max_value:
                max_value = value2
            if value2 < min_value:
                min_value = value2
            if current_sum == target:
                return min_value + max_value

    raise Exception('No solution')


if __name__ == '__main__':
    mydata = data_import('y2020/data/day9', cast=int)
    print('Input is', mydata[:10])
    print('Input length is', len(mydata))

    print('Solution of 1 is', solution1 := part1(mydata))
    print('Solution of 2 is', part2(mydata, target=solution1))
