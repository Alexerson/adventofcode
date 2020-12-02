from typing import List, Tuple

from adventofcode.utils import data_import


def convert_item(item: str) -> Tuple[int, int, str, str]:
    first_index, queue = item.split('-')
    second_index, letter, password = queue.split(" ")
    char = letter[:-1]
    return (int(first_index), int(second_index), char, password)


def check_first_policy(min_char, max_char, char, password):
    count = sum(a == char for a in password)
    return min_char <= count <= max_char


def check_second_policy(first, second, char, password):
    return (
        int(password[first - 1] == char) + int(password[second - 1] == char)
        == 1
    )


def part1(data: List[int]) -> int:
    return sum(
        check_first_policy(min_char, max_char, char, password)
        for min_char, max_char, char, password in data
    )


def part2(data: List[int]) -> int:
    return sum(check_second_policy(*args) for args in data)


if __name__ == '__main__':
    mydata = [
        convert_item(item) for item in data_import('y2020/data/day2', str)
    ]
    # print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
