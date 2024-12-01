from enum import Enum
from typing import List, Tuple

from adventofcode.utils import data_import


class Direction(Enum):
    N = 0
    S = 180
    E = 90
    W = 270

    F = 'F'
    L = 'L'
    R = 'R'

    def get_left(self, angle):
        if self in (self.F, self.L, self.R):
            return None

        return Direction((self.value - angle) % 360)

    def get_right(self, angle):
        if self in (self.F, self.L, self.R):
            return None

        return Direction((self.value + angle) % 360)

    def get_increment(self):
        return {
            self.N: (0, 1),
            self.S: (0, -1),
            self.E: (1, 0),
            self.W: (-1, 0),
        }[self]


def convert_data(data: List[str]) -> List[Tuple[Direction, int]]:
    return [(Direction[item[0]], int(item[1:])) for item in data]


def part1(data: List[Tuple[Direction, int]]) -> int:
    position = (0, 0)
    general_direction = Direction.E

    for move, value in data:
        if move == Direction.F:
            move = general_direction
        elif move == Direction.L:
            general_direction = general_direction.get_left(value)
            continue
        elif move == Direction.R:
            general_direction = general_direction.get_right(value)
            continue
        else:
            pass  # We don't change the general direction but use this move

        increment = move.get_increment()
        position = (
            position[0] + value * increment[0],
            position[1] + value * increment[1],
        )
    return abs(position[0]) + abs(position[1])


def part2(data: List[Tuple[Direction, int]]) -> int:
    waypoint_position = (10, 1)
    boat_position = (0, 0)

    for move, value in data:
        if move == Direction.F:
            boat_position = (
                boat_position[0] + value * waypoint_position[0],
                boat_position[1] + value * waypoint_position[1],
            )

        elif move == Direction.L:
            for _ in range(value // 90):  # Repeat multiple time if needed
                waypoint_position = (
                    -waypoint_position[1],
                    waypoint_position[0],
                )

        elif move == Direction.R:
            for _ in range(value // 90):
                waypoint_position = (
                    waypoint_position[1],
                    -waypoint_position[0],
                )

        else:
            increment = move.get_increment()
            waypoint_position = (
                waypoint_position[0] + value * increment[0],
                waypoint_position[1] + value * increment[1],
            )

    return abs(boat_position[0]) + abs(boat_position[1])


if __name__ == '__main__':
    mydata = convert_data(data_import('data/y2020/day12'))

    print('Data is: ', mydata[:10])

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
