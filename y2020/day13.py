from math import lcm
from typing import List, Literal, Tuple, Union

from adventofcode.utils import data_import


def convert_data(data) -> Tuple[int, List[Union[Literal['x'], int]]]:
    out: List[Union[Literal['x'], int]] = []
    for value in data[1].split(','):
        if value == 'x':
            out.append('x')
        else:
            out.append(int(value))
    return (int(data[0]), out)


def part1(data: Tuple[int, List[Union[Literal['x'], int]]]) -> int:
    timestamp, bus_ids = data[0], data[1]

    next_departs = []

    for bus_id in bus_ids:
        if bus_id == 'x':
            continue

        next_departs.append((bus_id, bus_id - (timestamp % bus_id)))

    next_departs = sorted(next_departs, key=lambda a: a[1])

    return next_departs[0][0] * next_departs[0][1]


def part2(data) -> int:

    timestamp = 0

    corrects = set()

    while True:
        errors = False

        for offset, bus_id in enumerate(data):
            if bus_id == 'x':
                continue

            if (timestamp + offset) % bus_id == 0:
                corrects.add(bus_id)
            else:
                errors = True

        if not errors:
            return timestamp

        # print(timestamp, corrects)
        timestamp += lcm(*corrects)


if __name__ == '__main__':
    mydata = convert_data(data_import('y2020/data/day13'))

    print('Data is: ', mydata[:10])

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata[1]))
