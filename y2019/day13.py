from utils import data_import
from intcode import Program
import math
import itertools
import collections

MAPPING = {
    0: ' ',
    1: '#',
    2: '*',
    3: '_',
    4: 'o'
}

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

    play = False

    while not program.finished:
        joystick = 0

        if play and position_ball and position_pad:
            if position_ball[0] > position_pad[0]:
                joystick = 1
            if position_ball[0] < position_pad[0]:
                joystick = -1

            inputs.append(joystick)
            play = False
            if debug:
                print(f'{inputs=} {position_ball=} {position_pad=} {current_score=}')

        x = program.run_until_output(inputs)
        y = program.run_until_output(inputs)
        tile_id = program.run_until_output(inputs)

        if tile_id is not None:
            if x == -1 and y == 0:
                current_score = tile_id
            else:
                tiles[(x, y)] = tile_id

                if tile_id == 3:
                    position_pad = [x, y]

                if tile_id == 4:
                    position_ball = [x, y]
                    play = True

    if debug:
        xs = [x for x, y in tiles.keys()]  
        ys = [y for x, y in tiles.keys()]  

        for y in range(min(ys), max(ys)+1):
            row = []
            for x in range(min(xs), max(xs)+1):
                row.append(MAPPING.get(tiles.get((x, y))))
            print(''.join(row))
            
    return current_score


if __name__ == '__main__':

    data = data_import('y2019/data/day13', cast=int, split_char=',')[0]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
