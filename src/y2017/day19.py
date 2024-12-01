from collections import deque

from utils import data_import

STRAIGHT = 1
TURN = 2


def convert(data):
    output = {}
    start = None
    for line_no, line in enumerate(data):
        for column_no, cell in enumerate(line):
            if cell == ' ':
                continue

            if line_no == 0:
                start = [line_no, column_no]

            if cell in ('|', '-'):
                output[(line_no, column_no)] = STRAIGHT

            elif cell == '+':
                output[(line_no, column_no)] = TURN

            else:
                output[(line_no, column_no)] = cell

    return start, output


def part1(data):
    position, plan = convert(data)

    current = plan[tuple(position)]
    direction = (1, 0)

    met = []
    steps = 0

    while current:
        if current == TURN:
            if direction[0] == 0:
                if (position[0] + 1, position[1]) in plan:
                    direction = (1, 0)
                else:
                    direction = (-1, 0)
            else:
                if (position[0], position[1] + 1) in plan:
                    direction = (0, 1)
                else:
                    direction = (0, -1)
        elif current != STRAIGHT:
            met.append(current)

        position[0] += direction[0]
        position[1] += direction[1]

        current = plan.get(tuple(position))
        steps += 1

    return ''.join(met), steps


if __name__ == '__main__':
    data_example = data_import('data/y2017/day19_example', str, rstrip=True)
    print('Solution is', part1(data_example))

    data_real = data_import('data/y2017/day19_real', str, rstrip=True)
    print('Solution is', part1(data_real))
