from typing import List

from adventofcode.utils import data_import


def convert_seat_to_id(seat: str) -> int:
    seat_binary = (
        seat.replace('F', '0')
        .replace('B', '1')
        .replace('L', '0')
        .replace('R', '1')
    )
    return int(seat_binary, 2)


def part1(data: List[str]) -> int:
    return max(convert_seat_to_id(seat) for seat in data)


def part2(data: List[str]) -> int:
    seat_ids = [convert_seat_to_id(seat) for seat in data]
    min_seat = min(seat_ids)
    max_seat = max(seat_ids)

    return next(iter(set(range(min_seat, max_seat)) - set(seat_ids)))


if __name__ == '__main__':
    mydata = data_import('data/y2020/day5')
    # print('Input is', mydata)
    # print('Seat ID for FFFBBBFRRR is', convert_seat_to_id('FFFBBBFRRR'))
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
