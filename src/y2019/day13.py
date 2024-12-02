import collections
from time import sleep

from src.utils import data_import

from .intcode import Program

MAPPING = {0: ' ', 1: '⬜', 2: 'O', 3: '▄', 4: '⚽'}


def part1(data):
    program = Program(data)
    tiles = []
    while not program.finished:
        x = program.run_until_output()
        y = program.run_until_output()
        tile_id = program.run_until_output()
        tiles.append((x, y, tile_id))

    return collections.Counter(a[2] for a in tiles)[2]


def part2(data, debug=False):
    data = list(data)
    data[0] = 2
    program = Program(data)
    tiles = {}
    current_score = 0

    inputs = []

    position_ball = None
    position_pad = None

    play = show = False

    step = 0

    while not program.finished:
        step += 1
        joystick = 0

        if play and position_ball and position_pad:
            if position_ball[0] > position_pad[0]:
                joystick = 1
            if position_ball[0] < position_pad[0]:
                joystick = -1

            inputs.append(joystick)
            play = False

        x = program.run_until_output(inputs)
        y = program.run_until_output(inputs)
        tile_id = program.run_until_output(inputs)

        if tile_id is not None:
            if x == -1 and y == 0:
                current_score = tile_id
            else:
                tiles[x, y] = tile_id

                if tile_id == 3:
                    position_pad = [x, y]
                    show = True

                if tile_id == 4:
                    position_ball = [x, y]
                    play = True

        if debug and show and position_ball and position_pad:
            xs = [x for x, y in tiles]
            ys = [y for x, y in tiles]

            rows = [f'{position_ball=} {position_pad=} {current_score=}'] + [
                ''.join(
                    MAPPING.get(tiles.get((x, y)), ' ')
                    for x in range(min(xs), max(xs) + 1)
                )
                for y in range(min(ys), max(ys) + 1)
            ]
            print('\n'.join(rows))
            print('\n')
            sleep(0.01)
            show = False

    return current_score


if __name__ == '__main__':
    data = data_import('data/y2019/day13', cast=int, split_char=',')[0]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data, debug=False))
