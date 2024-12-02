from time import sleep

from intcode import Program

from utils import data_import

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

MOVEMENT = {NORTH: (0, -1), SOUTH: (0, 1), EAST: (1, 0), WEST: (-1, 0)}

DISPLAY = {-1: ' ', 1: ' ', 0: '█', 2: '⦾', 3: '#', 4: '⚐'}


def display_space(space):
    space = space.copy()

    space[0, 0] = 4

    out = ['\nSpace:']

    xs = [x for x, y in space]
    ys = [y for x, y in space]

    out.append(
        '\n'.join(
            ''.join(
                DISPLAY[space.get((x, y), -1)]
                for x in range(min(xs), max(xs) + 1)
            )
            for y in range(min(ys), max(ys) + 1)
        ),
    )
    print('\n'.join(out))
    sleep(0.05)


def display_distances(distances):
    xs = [x for x, y in distances]
    ys = [y for x, y in distances]

    out = ['\nDistances:']
    out.append(
        '\n'.join(
            ' '.join(
                '{distance:3}'.format(distance=distances.get((x, y), ' '))
                for x in range(min(xs), max(xs) + 1)
            )
            for y in range(min(ys), max(ys) + 1)
        ),
    )
    print('\n'.join(out))
    sleep(0.05)


def explore_space(data):
    program = Program(data)
    position = [0, 0]
    space = {tuple(position): 0}

    last_correct_directions = []
    ignore_direction = False

    distances = {(0, 0): 0}

    while not program.finished:
        if (position[0], position[1] - 1) not in space:
            direction = NORTH

        elif (position[0] + 1, position[1]) not in space:
            direction = EAST

        elif (position[0], position[1] + 1) not in space:
            direction = SOUTH

        elif (position[0] - 1, position[1]) not in space:
            direction = WEST

        else:
            if not last_correct_directions:
                break
            last_correct_direction = last_correct_directions.pop()
            if last_correct_direction in {EAST, SOUTH}:
                direction = last_correct_direction - 1
            else:
                direction = last_correct_direction + 1
            ignore_direction = True

        x = program.run_until_output([direction])

        movement = MOVEMENT[direction]
        space[position[0] + movement[0], position[1] + movement[1]] = x

        if x != 0:
            distance = distances[tuple(position)]
            if not ignore_direction:
                last_correct_directions.append(direction)
            ignore_direction = False
            position[0] += movement[0]
            position[1] += movement[1]

            if tuple(position) not in distances:
                distances[tuple(position)] = distance + 1

    return space, distances


def part1(data, debug=True):
    space, distances = explore_space(data)

    if debug:
        display_space(space)
        display_distances(distances)

    oxygene = next((x, y) for (x, y), value in space.items() if value == 2)

    if debug:
        print('Furthest place is at', max(distances.values()))
    return distances.get(oxygene), max(distances.values())


def part2(data):
    distance_to_o2, furthest_distance = part1(data, debug=False)
    print(
        'We can do this one manually. '
        'First find the furthest point in the part 1'
        f' map debug ({furthest_distance}).\n'
        'Then find where the path to the highest point branch '
        'from the path to the oxygen.\n'
        'Finally, do this simple math:  '
        '(distance_to_O2 + furthest_distance) - 2 * (distance_to_branching)',
    )
    branching = input("What's the branch value?")
    return distance_to_o2 + furthest_distance - 2 * int(branching)


if __name__ == '__main__':
    data = data_import('data/y2019/day15', cast=int, split_char=',')[0]
    print('Solution of 1 is', part1(data)[0])
    print('Solution of 2 is', part2(data))

# 252 - 156  # Pour aller au carrefour
# 410 - 156  # Pour aller au bout
