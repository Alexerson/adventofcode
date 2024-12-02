import collections
import operator

from utils import data_import

STRAIGHT = 1
TURN_ONE = 2
TURN_TWO = 3
INTERSECTION = 4

track_match = {
    '+': INTERSECTION,
    '/': TURN_ONE,
    '\\': TURN_TWO,
    '|': STRAIGHT,
    '-': STRAIGHT,
}

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

directions_match = {'>': RIGHT, '<': LEFT, '^': UP, 'v': DOWN}

CYCLE_LEFT = 0
CYCLE_STRAIGHT = 1
CYCLE_RIGHT = 2


def build_tracks(data):
    tracks = {}
    carts = []

    for line_i, line in enumerate(data):
        for column_i, cell in enumerate(line):
            if cell == ' ':
                continue

            direction = directions_match.get(cell)
            if direction is not None:
                carts.append([column_i, line_i, direction, CYCLE_LEFT, False])
                tracks[column_i, line_i] = STRAIGHT

            else:
                tracks[column_i, line_i] = track_match[cell]

    return tracks, carts


def move_one_cart(cart, tracks):
    if cart[2] == UP:
        cart[1] -= 1
        new_track = tracks[cart[0], cart[1]]
        if new_track == TURN_ONE:
            cart[2] = RIGHT
        elif new_track == TURN_TWO:
            cart[2] = LEFT
        elif new_track == INTERSECTION:
            cycle = cart[3]
            if cycle == CYCLE_LEFT:
                cart[2] = LEFT
                cart[3] = CYCLE_STRAIGHT
            elif cycle == CYCLE_STRAIGHT:
                cart[3] = CYCLE_RIGHT
            elif cycle == CYCLE_RIGHT:
                cart[2] = RIGHT
                cart[3] = CYCLE_LEFT

    elif cart[2] == RIGHT:
        cart[0] += 1
        new_track = tracks[cart[0], cart[1]]
        if new_track == TURN_ONE:
            cart[2] = UP
        elif new_track == TURN_TWO:
            cart[2] = DOWN
        elif new_track == INTERSECTION:
            cycle = cart[3]
            if cycle == CYCLE_LEFT:
                cart[2] = UP
                cart[3] = CYCLE_STRAIGHT
            elif cycle == CYCLE_STRAIGHT:
                cart[3] = CYCLE_RIGHT
            elif cycle == CYCLE_RIGHT:
                cart[2] = DOWN
                cart[3] = CYCLE_LEFT

    elif cart[2] == DOWN:
        cart[1] += 1
        new_track = tracks[cart[0], cart[1]]
        if new_track == TURN_ONE:
            cart[2] = LEFT
        elif new_track == TURN_TWO:
            cart[2] = RIGHT
        elif new_track == INTERSECTION:
            cycle = cart[3]
            if cycle == CYCLE_LEFT:
                cart[2] = RIGHT
                cart[3] = CYCLE_STRAIGHT
            elif cycle == CYCLE_STRAIGHT:
                cart[3] = CYCLE_RIGHT
            elif cycle == CYCLE_RIGHT:
                cart[2] = LEFT
                cart[3] = CYCLE_LEFT

    elif cart[2] == LEFT:
        cart[0] -= 1
        new_track = tracks[cart[0], cart[1]]
        if new_track == TURN_ONE:
            cart[2] = DOWN
        elif new_track == TURN_TWO:
            cart[2] = UP
        elif new_track == INTERSECTION:
            cycle = cart[3]
            if cycle == CYCLE_LEFT:
                cart[2] = DOWN
                cart[3] = CYCLE_STRAIGHT
            elif cycle == CYCLE_STRAIGHT:
                cart[3] = CYCLE_RIGHT
            elif cycle == CYCLE_RIGHT:
                cart[2] = UP
                cart[3] = CYCLE_LEFT


def show_tracks(carts, tracks):
    carts_coords = {(cart[0], cart[1]) for cart in carts}

    max_column = max(coord[0] for coord in tracks)
    max_line = max(coord[1] for coord in tracks)
    for line in range(max_line + 1):
        line_out = ''
        for column in range(max_column + 1):
            if (column, line) in carts_coords:
                line_out += '#'

            elif (column, line) in tracks:
                line_out += '.'

            else:
                line_out += ' '
        print(line_out)


def get_collision(carts):
    counter = collections.Counter(
        (cart[0], cart[1]) for cart in carts if not cart[4]
    )

    return [cart for cart in carts if counter[cart[0], cart[1]] > 1]


def part1(data):
    tracks, carts = build_tracks(data)

    while True:
        carts.sort(key=operator.itemgetter(1, 0))
        for cart in carts:
            move_one_cart(cart, tracks)
            # We need to check collisions at each step to not miss '-><-'
            collisions = get_collision(carts)
            if collisions:
                return collisions


def part2(data):
    tracks, carts = build_tracks(data)

    while True:
        carts.sort(key=operator.itemgetter(1, 0))
        for cart in carts:
            if cart[4]:
                continue
            move_one_cart(cart, tracks)
            # We need to check collisions at each step to not miss '-><-'
            collisions = get_collision(carts)
            for collision in collisions:
                collision[4] = True
        # But we check the counts only at the end of the tick
        if sum(not cart[4] for cart in carts) <= 1:
            return [cart for cart in carts if not cart[4]]


if __name__ == '__main__':
    data_example = data_import('data/day13_example', rstrip=True)
    print('Example:')
    print('Solution of 1 is', part1(data_example))

    data_example2 = data_import('data/day13_example2', rstrip=True)
    print('Solution of 2 is', part2(data_example2))

    print('Real:')
    data = data_import('data/day13_real', rstrip=True)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
