from enum import Enum
from typing import NamedTuple

from utils import data_import


class Position:
    x: int = 0
    y: int = 0
    aim: int = 0

    def apply(self, action: 'Action', with_aim: bool = False):
        action.verb.apply(self, action.value, with_aim)


class Verb(Enum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

    def apply(
        self, position: Position, value: int, with_aim: bool = False
    ) -> None:

        if not with_aim:

            if self == Verb.FORWARD:
                position.x += value
            elif self == Verb.DOWN:
                position.y -= value
            elif self == Verb.UP:
                position.y += value

        else:

            if self == Verb.FORWARD:
                position.x += value
                position.y -= position.aim * value
            elif self == Verb.DOWN:
                position.aim += value
            elif self == Verb.UP:
                position.aim -= value


class Action(NamedTuple):
    verb: Verb
    value: int


def convert_data(data: list[list[str]]) -> list[Action]:
    return [Action(Verb(item[0]), int(item[1])) for item in data]


def part1(data: list[Action]) -> int:
    position = Position()

    for action in data:
        position.apply(action)

    return -position.x * position.y


def part2(data: list[Action]) -> int:
    position = Position()

    for action in data:
        position.apply(action, with_aim=True)

    return -position.x * position.y


if __name__ == '__main__':
    mydata = data_import('y2021/data/day2', split_char=' ')
    print('Input is', mydata)
    mydata = convert_data(mydata)
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
