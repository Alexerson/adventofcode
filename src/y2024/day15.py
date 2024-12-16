from dataclasses import dataclass
from time import sleep

from src.utils import data_import


@dataclass
class Warehouse:
    robot: tuple[int, int]
    boxes: set[tuple[int, int]]
    walls: set[tuple[int, int]]

    @classmethod
    def from_data(cls, data: list[str]) -> tuple['Warehouse', str]:
        robot: tuple[int, int] | None = None
        boxes: set[tuple[int, int]] = set()
        walls: set[tuple[int, int]] = set()
        moves = ''

        for row_no, row in enumerate(data):
            if row.startswith('#'):
                for column_no, cell in enumerate(row):
                    if cell == '#':
                        walls.add((column_no, row_no))
                    elif cell == '@':
                        robot = (column_no, row_no)
                    elif cell == 'O':
                        boxes.add((column_no, row_no))
            else:
                moves += row

        return cls(robot=robot, boxes=boxes, walls=walls), moves

    def move_robot(self, move: str) -> None:
        match move:
            case '^':
                move_tuple = [0, -1]
            case 'v':
                move_tuple = [0, 1]
            case '>':
                move_tuple = [1, 0]
            case '<':
                move_tuple = [-1, 0]

        if (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        ) in self.walls:
            return

        if (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        ) in self.boxes:
            # I need to find if at the end of the row of boxes,
            # we have a wall or an empty space
            spaces = 1
            while (
                self.robot[0] + move_tuple[0] * spaces,
                self.robot[1] + move_tuple[1] * spaces,
            ) in self.boxes:
                spaces += 1

            # If it’s a wall, we can’t move
            if (
                self.robot[0] + move_tuple[0] * spaces,
                self.robot[1] + move_tuple[1] * spaces,
            ) in self.walls:
                return

            # If it’s an empty space, we can move
            self.boxes.remove((
                self.robot[0] + move_tuple[0],
                self.robot[1] + move_tuple[1],
            ))
            self.boxes.add((
                self.robot[0] + move_tuple[0] * spaces,
                self.robot[1] + move_tuple[1] * spaces,
            ))

        self.robot = (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        )

    def display(self) -> None:
        width = max(item[0] for item in self.walls)
        height = max(item[1] for item in self.walls)
        for y in range(height + 1):
            for x in range(width + 1):
                if (x, y) in self.walls:
                    print('#', end='')
                elif (x, y) == self.robot:
                    print('@', end='')
                elif (x, y) in self.boxes:
                    print('O', end='')
                else:
                    print(' ', end='')
            print()

    def gps_sum(self) -> int:
        return sum(x + y * 100 for x, y in self.boxes)


@dataclass
class WarehouseBis:
    robot: tuple[int, int]
    boxes: set[tuple[int, int]]
    walls: set[tuple[int, int]]

    @classmethod
    def from_data(cls, data: list[str]) -> tuple['Warehouse', str]:
        robot: tuple[int, int] | None = None
        boxes: set[tuple[int, int]] = set()
        walls: set[tuple[int, int]] = set()
        moves = ''

        for row_no, row in enumerate(data):
            if row.startswith('#'):
                for column_no, cell in enumerate(row):
                    if cell == '#':
                        walls.add((2 * column_no, row_no))
                        walls.add((2 * column_no + 1, row_no))
                    elif cell == '@':
                        robot = (2 * column_no, row_no)
                    elif cell == 'O':
                        boxes.add((2 * column_no, row_no))
            else:
                moves += row

        return cls(robot=robot, boxes=boxes, walls=walls), moves

    def move_robot(self, move: str) -> None:
        match move:
            case '^':
                move_tuple = [0, -1]
            case 'v':
                move_tuple = [0, 1]
            case '>':
                move_tuple = [1, 0]
            case '<':
                move_tuple = [-1, 0]

        if (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        ) in self.walls:
            return

        if (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        ) in self.boxes:
            # I need to find if at the end of the row of boxes,
            # we have a wall or an empty space
            spaces = 1
            while (
                self.robot[0] + move_tuple[0] * spaces,
                self.robot[1] + move_tuple[1] * spaces,
            ) in self.boxes:
                spaces += 1

            # If it’s a wall, we can’t move
            if (
                self.robot[0] + move_tuple[0] * spaces,
                self.robot[1] + move_tuple[1] * spaces,
            ) in self.walls:
                return

            # If it’s an empty space, we can move
            self.boxes.remove((
                self.robot[0] + move_tuple[0],
                self.robot[1] + move_tuple[1],
            ))
            self.boxes.add((
                self.robot[0] + move_tuple[0] * spaces,
                self.robot[1] + move_tuple[1] * spaces,
            ))

        self.robot = (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        )

    def display(self) -> None:
        width = max(item[0] for item in self.walls)
        height = max(item[1] for item in self.walls)
        for y in range(height + 1):
            for x in range(width + 1):
                if (x, y) in self.walls:
                    print('#', end='')
                elif (x, y) == self.robot:
                    print('@', end='')
                elif (x, y) in self.boxes:
                    print('[', end='')
                elif (x - 1, y) in self.boxes:
                    print(']', end='')
                else:
                    print(' ', end='')
            print()

    def gps_sum(self) -> int:
        return sum(x + y * 100 for x, y in self.boxes)


def part1(data: list[str]) -> int:
    warehouse, moves = Warehouse.from_data(data)
    for move in moves:
        warehouse.move_robot(move)
        # warehouse.display()
        # sleep(0.01)
    return warehouse.gps_sum()


def part2(data: list[str]) -> int:
    warehouse, moves = WarehouseBis.from_data(data)
    warehouse.display()
    for move in moves:
        warehouse.move_robot(move)
        warehouse.display()
        sleep(0.01)
    return warehouse.gps_sum()


if __name__ == '__main__':
    example_easy = data_import('data/y2024/day15-example-easy')
    example_easy_2 = data_import('data/y2024/day15-example-easy-2')
    example = data_import('data/y2024/day15-example')
    mydata = data_import('data/y2024/day15')

    # part1(example_easy)
    # assert_result(part1(example), 10092)
    # print('Solution of 1 is', part1(mydata))  # 9 min
    part2(example_easy_2)
    # assert_result(part2(example), 9021)
    # print('Solution of 2 is', part2(mydata))  # 35 min
