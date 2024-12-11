from functools import cache
from math import log10
from typing import cast

from src.utils import assert_result, data_import


@cache  # type: ignore[misc]
def len_generated_stones(stone: int, iterations: int) -> int:
    if iterations == 0:
        return 1

    if stone == 0:
        return len_generated_stones(1, iterations=iterations - 1)

    magnitude = int(log10(stone) + 1)
    if magnitude % 2 == 0:
        multiplier = cast('int', pow(10, magnitude // 2))
        first = stone // multiplier
        second = stone % multiplier

        return len_generated_stones(
            first, iterations - 1
        ) + len_generated_stones(second, iterations - 1)

    return len_generated_stones(stone * 2024, iterations - 1)


def part1(stones: list[int], iterations: int = 25) -> int:
    return sum(len_generated_stones(s, iterations=iterations) for s in stones)


def part2(stones: list[int]) -> int:
    return part1(stones, iterations=75)


if __name__ == '__main__':
    mydata = [125, 17]

    assert_result(part1(mydata), 55312)

    mydata = data_import('data/y2024/day11', int, split_char=' ')[0]
    print('Solution of 1 is', part1(mydata))  # 7 min 26
    print('Solution of 2 is', part2(mydata))  # 16 min 45
