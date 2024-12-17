from dataclasses import dataclass
from time import sleep

from utils import data_import, assert_result


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

    def move_robot(self, move: str) -> bool:
        match move:
            case '^':
                move_tuple = [0, -1]
            case 'v':
                move_tuple = [0, 1]
            case '>':
                move_tuple = [1, 0]
            case '<':
                move_tuple = [-1, 0]

        moving_boxes: set[tuple[int, int]] = set()
        moving_cells: set[tuple[int, int]] = {self.robot}

        while moving_cells:
            cell_to_test = moving_cells.pop()

            cell_to_test = (
                cell_to_test[0] + move_tuple[0],
                cell_to_test[1] + move_tuple[1],
            )

            # As soon as we hit a wall, we're done
            if cell_to_test in self.walls:
                return False

            # Otherwise we add existing boxes to the cells to test and move
            if cell_to_test in self.boxes and cell_to_test not in moving_boxes:
                moving_boxes.add(cell_to_test)
                moving_cells.add(cell_to_test)
                moving_cells.add((cell_to_test[0] + 1, cell_to_test[1]))

            if (cell_to_test[0] - 1, cell_to_test[1]) in self.boxes and (
                cell_to_test[0] - 1,
                cell_to_test[1],
            ) not in moving_boxes:
                moving_boxes.add((cell_to_test[0] - 1, cell_to_test[1]))
                moving_cells.add((cell_to_test[0] - 1, cell_to_test[1]))
                moving_cells.add(cell_to_test)

        # Now we move everyone!
        for box in moving_boxes:
            self.boxes.remove(box)
        for box in moving_boxes:
            self.boxes.add((
                box[0] + move_tuple[0],
                box[1] + move_tuple[1],
            ))

        # And now the robot moves as well
        self.robot = (
            self.robot[0] + move_tuple[0],
            self.robot[1] + move_tuple[1],
        )
        return True

    def display(self) -> None:
        out = ''
        width = max(item[0] for item in self.walls)
        height = max(item[1] for item in self.walls)
        for y in range(height + 1):
            for x in range(width + 1):
                if (x, y) in self.walls:
                    out += '#'
                elif (x, y) == self.robot:
                    out += '@'
                elif (x, y) in self.boxes:
                    out += '['
                elif (x - 1, y) in self.boxes:
                    out += ']'
                else:
                    out += ' '
            out += '\n'
        print(out)

    def gps_sum(self) -> int:
        return sum(x + y * 100 for x, y in self.boxes)


def part1(data: list[str]) -> int:
    warehouse, moves = Warehouse.from_data(data)
    for move in moves:
        warehouse.move_robot(move)
    return warehouse.gps_sum()


def part2(data: list[str], display_fps: int | None = None) -> int:
    warehouse, moves = WarehouseBis.from_data(data)
    if display_fps:
        warehouse.display()
    for move in moves:
        moved = warehouse.move_robot(move)
        if moved and display_fps:
            warehouse.display()
            sleep(1 / display_fps)
    if display_fps:
        warehouse.display()
    return warehouse.gps_sum()


if __name__ == '__main__':
    example = data_import('data/y2024/day15-example')
    mydata = data_import('data/y2024/day15')

    assert_result(part1(example), 10092)
    print('Solution of 1 is', part1(mydata))
    assert_result(part2(example), 9021)
    print('Solution of 2 is', part2(mydata))
