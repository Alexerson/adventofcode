from src.utils import data_import


def next_step(
    position: tuple[int, int, str], walls: set[tuple[int, int]]
) -> tuple[int, int, str]:
    move = (0, 0)
    match position[2]:
        case 'N':
            move = (0, -1)
            new_direction = 'E'
        case 'S':
            move = (0, 1)
            new_direction = 'W'
        case 'E':
            move = (1, 0)
            new_direction = 'S'
        case 'W':
            move = (-1, 0)
            new_direction = 'N'

    in_front = position[0] + move[0], position[1] + move[1]
    if in_front not in walls:
        return (in_front[0], in_front[1], position[2])

    return (position[0], position[1], new_direction)


def part1(data: list[str]) -> int:
    walls: set[tuple[int, int]] = set()
    position = (0, 0, 'N')

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            if c == '^':
                position = (x, y, 'N')

    visited: set[tuple[int, int]] = set()

    width = len(data[0])
    height = len(data)

    while 0 <= position[0] <= width - 1 and 0 <= position[1] <= height - 1:
        visited.add((position[0], position[1]))
        position = next_step(position, walls)

    return len(visited)


def is_loop(
    position: tuple[int, int, str],
    walls: set[tuple[int, int]],
    width: int,
    height: int,
) -> bool:
    visited: set[tuple[int, int, str]] = set()

    while (
        position not in visited
        and 0 <= position[0] <= width - 1
        and 0 <= position[1] <= height - 1
    ):
        visited.add(position)
        position = next_step(position, walls)

    return position in visited


def part2(data: list[str]) -> int:
    walls: set[tuple[int, int]] = set()
    initial_position = (0, 0, 'N')

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            if c == '^':
                initial_position = (x, y, 'N')

    width = len(data[0])
    height = len(data)

    positions_to_test: set[tuple[int, int]] = set()

    position = initial_position
    while 0 <= position[0] <= width - 1 and 0 <= position[1] <= height - 1:
        positions_to_test.add((position[0], position[1]))
        position = next_step(position, walls)

    total = 0
    for obstacle in positions_to_test:
        new_walls = walls.copy()
        new_walls.add(obstacle)
        if is_loop(initial_position, new_walls, width, height):
            total += 1

    return total


if __name__ == '__main__':
    mydata = data_import('data/y2024/day6-example')
    assert part1(mydata) == 41
    assert part2(mydata) == 6

    mydata = data_import('data/y2024/day6')
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
