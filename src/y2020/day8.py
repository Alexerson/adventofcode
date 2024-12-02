from copy import deepcopy
from typing import List, Tuple

from utils import data_import


class NoFinishError(Exception):
    pass


def convert_data(data: List[List[str]]) -> List[Tuple[str, int]]:
    return [(a, int(b)) for a, b in data]


def run_program(data: List[Tuple[str, int]]) -> Tuple[bool, int]:
    data_len = len(data)

    accumulator = 0
    pointer = 0

    executed = set()

    while True:
        if pointer in executed:
            return False, accumulator

        if pointer >= data_len:
            return True, accumulator

        ope, value = data[pointer]

        executed.add(pointer)

        if ope == 'acc':
            accumulator += value
            pointer += 1

        if ope == 'jmp':
            pointer += value

        if ope == 'nop':
            pointer += 1


def part1(data) -> int:
    return run_program(data)[1]


def part2(data) -> int:
    for index, (ope, value) in enumerate(data):
        if ope == 'acc':
            continue

        if ope == 'nop':
            new_prog = deepcopy(data)
            new_prog[index] = ('jmp', value)
        if ope == 'jmp':
            new_prog = deepcopy(data)
            new_prog[index] = ('nop', value)

        finished, result = run_program(new_prog)

        if finished:
            return result

    raise NoFinishError


if __name__ == '__main__':
    mydata = convert_data(data_import('data/y2020/day8', split_char=' '))
    print('Input is', mydata[:10])
    print('Input length is', len(mydata))

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
