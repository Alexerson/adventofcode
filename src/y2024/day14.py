from dataclasses import dataclass
from math import prod

from PIL import Image

from src.utils import assert_result, data_import


@dataclass
class Robot:
    x: int
    y: int

    vx: int
    vy: int

    @classmethod
    def from_raw(cls, raw: str) -> 'Robot':
        p, v = raw.split(' ')
        x, y = p[2:].split(',')
        vx, vy = v[2:].split(',')

        return cls(int(x), int(y), int(vx), int(vy))

    def move(self, room: tuple[int, int], steps: int = 1) -> None:
        self.x = (self.x + steps * self.vx) % room[0]
        self.y = (self.y + steps * self.vy) % room[1]


def part1(data: list[str], room: tuple[int, int]) -> int:
    robots = [Robot.from_raw(x) for x in data if x.strip()]

    for robot in robots:
        robot.move(room, 100)

    quandrants = [0, 0, 0, 0]

    half = room[0] // 2, room[1] // 2

    for robot in robots:
        if robot.x < half[0] and robot.y < half[1]:
            quandrants[0] += 1
        if robot.x > half[0] and robot.y < half[1]:
            quandrants[1] += 1
        if robot.x < half[0] and robot.y > half[1]:
            quandrants[2] += 1
        if robot.x > half[0] and robot.y > half[1]:
            quandrants[3] += 1

    return prod(quandrants)


def display_room(data: list[Robot], room: tuple[int, int]) -> None:
    canvas = Image.new('L', room)

    for y in range(room[1]):
        for x in range(room[0]):
            robots_count = sum(robot.x == x and robot.y == y for robot in data)
            if robots_count > 0:
                canvas.putpixel((x, y), max(50 * robots_count, 255))
    canvas.show()


def part2(data: list[str], room: tuple[int, int]) -> int:
    robots = [Robot.from_raw(x) for x in data if x.strip()]
    len_robots = len(robots)
    steps = 0
    while len({(robot.x, robot.y) for robot in robots}) != len_robots:
        steps += 1
        for robot in robots:
            robot.move(room)
    return steps


if __name__ == '__main__':
    example = data_import('data/y2024/day14-example')
    room_example = 11, 7
    mydata = data_import('data/y2024/day14')
    room = 101, 103

    assert_result(part1(example, room_example), 12)
    print('Solution of 1 is', part1(mydata, room))  # 9 min
    print('Solution of 2 is', part2(mydata, room))  # 35 min
