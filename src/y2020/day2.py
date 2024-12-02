from typing import List, NamedTuple

from utils import data_import


class Record(NamedTuple):
    first_number: int
    second_number: int
    letter: str
    password: str


def convert_item(item: str) -> Record:
    numbers, letter, password = item.split(' ')
    first_number, second_number = numbers.split('-')
    return Record(int(first_number), int(second_number), letter[0], password)


def check_first_policy(record: Record) -> bool:
    count = record.password.count(record.letter)
    return record.first_number <= count <= record.second_number


def check_second_policy(record: Record) -> bool:
    first_char = record.password[record.first_number - 1]
    second_char = record.password[record.second_number - 1]
    return (first_char == record.letter) ^ (second_char == record.letter)


def part1(data: List[Record]) -> int:
    return sum(check_first_policy(record) for record in data)


def part2(data: List[Record]) -> int:
    return sum(check_second_policy(record) for record in data)


if __name__ == '__main__':
    mydata = [
        convert_item(item) for item in data_import('data/y2020/day2', str)
    ]
    # print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
