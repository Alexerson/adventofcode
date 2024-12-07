from operator import add, mul
from typing import Callable

from src.utils import data_import


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def is_solvable(
    test_value: int,
    values: list[int],
    operations: list[Callable[[int, int], int]],
) -> bool:
    if len(values) == 1:
        return values[0] == test_value

    a, b, *queue = values

    if a > test_value:  # If we are already too big, just give up
        return False

    return any(
        is_solvable(test_value, [operation(a, b), *queue], operations)
        for operation in operations
    )


def part1(data: list[list[str]]) -> int:
    total = 0
    operations: list[Callable[[int, int], int]] = [add, mul]  # type: ignore[misc]
    for line in data:
        test_value = int(line[0][:-1])
        values = [int(x) for x in line[1:]]

        if is_solvable(test_value, values, operations=operations):
            total += test_value

    return total


def part2(data: list[list[str]]) -> int:
    total = 0
    operations: list[Callable[[int, int], int]] = [add, mul, concat]  # type: ignore[misc]
    for line in data:
        test_value = int(line[0][:-1])
        values = [int(x) for x in line[1:]]

        if is_solvable(test_value, values, operations=operations):
            total += test_value

    return total


if __name__ == '__main__':
    mydata = data_import('data/y2024/day7-example', split_char=' ')
    assert part1(mydata) == 3749
    assert part2(mydata) == 11387

    mydata = data_import('data/y2024/day7', split_char=' ')
    print('Solution of 1 is', part1(mydata))  # 14 min
    print('Solution of 2 is', part2(mydata))  # 15 min 40
