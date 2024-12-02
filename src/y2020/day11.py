from copy import deepcopy
from typing import Dict, List, Tuple

from utils import data_import


class Room:
    seats: Dict[Tuple[int, int], bool]
    ncol: int
    nrow: int

    def __init__(self, data: List[str]) -> None:
        self.seats: Dict[Tuple[int, int], bool] = {}

        self.nrow = len(data)
        self.ncol = len(data[0])

        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                if cell == '.':
                    continue

                self.seats[i, j] = cell == '#'

    def _cell_to_str(self, i: int, j: int) -> str:
        status = self.seats.get((i, j))

        if status is None:
            return '.'

        if status:
            return '#'
        return 'L'

    def __str__(self) -> str:
        return '\n'.join(
            ''.join(self._cell_to_str(i, j) for j in range(self.ncol))
            for i in range(self.nrow)
        )

    def count_occupied(self) -> int:
        return sum(seat for seat in self.seats.values())

    def rule1(self, i: int, j: int) -> bool:
        if (i, j) not in self.seats:
            msg = 'Not a seat'
            raise AttributeError(msg)

        directions = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )

        occupied = sum(
            self.seats.get((i + i_, j + j_), 0) for i_, j_ in directions
        )
        if occupied == 0:
            return True

        if occupied >= 4:
            return False

        return self.seats[i, j]

    def rule2(self, i: int, j: int) -> bool:
        if (i, j) not in self.seats:
            msg = 'Not a seat'
            raise AttributeError(msg)

        directions = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )

        occupied = 0

        for i_, j_ in directions:
            step = 1

            while (
                0 <= i + step * i_ < self.nrow
                and 0 <= j + step * j_ < self.ncol
            ):
                seat = self.seats.get((i + step * i_, j + step * j_))

                if seat is None:
                    step += 1
                    continue

                occupied += seat
                break

        if occupied == 0:
            return True

        if occupied >= 5:
            return False

        return self.seats[i, j]

    def run_once(self, rule) -> None:
        new_seats = {}
        for i, j in self.seats:
            new_seats[i, j] = rule(i, j)

        self.seats = new_seats


def part1(room: Room) -> int:
    seen = set()
    steps = 0

    while str(room) not in seen:
        seen.add(str(room))
        room.run_once(room.rule1)
        steps += 1

    print(f'Converged in {steps} steps')

    return room.count_occupied()


def part2(room: Room) -> int:
    seen = set()
    steps = 0

    while str(room) not in seen:
        seen.add(str(room))
        room.run_once(room.rule2)
        steps += 1

    print(f'Converged in {steps} steps')

    return room.count_occupied()


if __name__ == '__main__':
    mydata = Room(data_import('data/y2020/day11'))

    print('Solution of 1 is', part1(deepcopy(mydata)))
    print('Solution of 2 is', part2(deepcopy(mydata)))
