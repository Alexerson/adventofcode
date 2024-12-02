import contextlib

from intcode import Program

from utils import data_import


def part1(data):
    program = Program(data)

    white_panels = set()
    position = (0, 0)
    direction = 'U'
    painted = set()

    while not program.finished:
        current_color = int(position in white_panels)

        new_color = program.run_until_output([current_color])
        new_direction = program.run_until_output()

        painted.add(position)
        if new_color == 1:
            white_panels.add(position)
        else:
            with contextlib.suppress(KeyError):
                white_panels.remove(position)

        if new_direction == 0:  # Turn left:
            if direction == 'U':
                position = (position[0] - 1, position[1])
                direction = 'L'
            elif direction == 'L':
                position = (position[0], position[1] - 1)
                direction = 'D'
            elif direction == 'D':
                position = (position[0] + 1, position[1])
                direction = 'R'
            elif direction == 'R':
                position = (position[0], position[1] + 1)
                direction = 'U'
        elif direction == 'U':
            position = (position[0] + 1, position[1])
            direction = 'R'
        elif direction == 'L':
            position = (position[0], position[1] + 1)
            direction = 'U'
        elif direction == 'D':
            position = (position[0] - 1, position[1])
            direction = 'L'
        elif direction == 'R':
            position = (position[0], position[1] - 1)
            direction = 'D'

    return len(painted)


def part2(data):
    program = Program(data)

    position = (0, 0)
    direction = 'U'
    white_panels = {position}

    while not program.finished:
        current_color = int(position in white_panels)

        new_color = program.run_until_output([current_color])
        new_direction = program.run_until_output()

        if new_color == 1:
            white_panels.add(position)
        else:
            with contextlib.suppress(KeyError):
                white_panels.remove(position)

        if new_direction == 0:  # Turn left:
            if direction == 'U':
                position = (position[0] - 1, position[1])
                direction = 'L'
            elif direction == 'L':
                position = (position[0], position[1] - 1)
                direction = 'D'
            elif direction == 'D':
                position = (position[0] + 1, position[1])
                direction = 'R'
            elif direction == 'R':
                position = (position[0], position[1] + 1)
                direction = 'U'
        elif direction == 'U':
            position = (position[0] + 1, position[1])
            direction = 'R'
        elif direction == 'L':
            position = (position[0], position[1] + 1)
            direction = 'U'
        elif direction == 'D':
            position = (position[0] - 1, position[1])
            direction = 'L'
        elif direction == 'R':
            position = (position[0], position[1] - 1)
            direction = 'D'

    xs = [a[0] for a in white_panels]
    ys = [a[1] for a in white_panels]

    for y in range(max(ys), min(ys) - 1, -1):
        out = []
        for x in range(min(xs), max(xs) + 1):
            if (x, y) in white_panels:
                out.append('#')
            else:
                out.append(' ')
        print(''.join(out))


if __name__ == '__main__':
    data = data_import('data/y2019/day11', cast=int, split_char=',')[0]

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is')
    part2(data)
