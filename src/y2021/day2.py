from enum import Enum
from typing import NamedTuple

from utils import data_import


class Position:
    x: int = 0
    y: int = 0
    aim: int = 0

    def apply(self, action: 'Action', with_aim: bool = False) -> 'Position':
        action.apply(self, with_aim)


class Verb(Enum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'


class Action(NamedTuple):
    verb: Verb
    value: int

    def apply(self, position: Position, with_aim: bool = False) -> None:
        match (self.verb, with_aim):
            case Verb.FORWARD, False:
                position.x += self.value
            case Verb.DOWN, False:
                position.y -= self.value
            case Verb.UP, False:
                position.y += self.value

            case Verb.FORWARD, True:
                position.x += self.value
                position.y -= position.aim * self.value
            case Verb.DOWN, True:
                position.aim += self.value
            case Verb.UP, True:
                position.aim -= self.value


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
    mydata = data_import('data/y2021/day2', split_char=' ')
    print('Input is', mydata)
    mydata = convert_data(mydata)
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
