import math
import random

from utils import data_import


def convert_to_nanobots(data):
    bots = []
    for line in data:
        bots.append(
            (
                (int(line[0][5:]), int(line[1]), int(line[2][:-1])),
                int(line[3].split("=")[1]),
            )
        )
    return bots


def distance(a, b):
    return sum(abs(i - j) for i, j in zip(a, b))


def part1(data):
    bots = convert_to_nanobots(data)

    bots.sort(key=lambda a: a[1], reverse=True)

    largest = bots[0]

    start, radius = largest

    return get_in_range_count(bots, start, radius)


def get_in_range_count(bots, position, radius=None):
    return sum(distance(bot[0], position) <= (radius or bot[1]) for bot in bots)


def part2(data, position=None):
    bots = convert_to_nanobots(data)

    if position is None:
        position = (0, 0, 0)

    maximum = (
        get_in_range_count(bots, position),
        -distance(position, (0, 0, 0)),
    )
    general_maximum = maximum
    general_position = position

    stalled = 0
    temperature_init = 100000
    temperature = temperature_init

    while True:
        move = random.choice(
            [
                (0, 1, 0),
                (0, -1, 0),
                (-1, 0, 0),
                (1, 0, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]
        )
        step = int(random.random() * 1000000) + 1
        new_position = (
            position[0] + step * move[0],
            position[1] + step * move[1],
            position[2] + step * move[2],
        )

        new_value = (
            get_in_range_count(bots, new_position),
            -distance(new_position, (0, 0, 0)),
        )

        delta_e = maximum[0] - new_value[0]

        # delta_e = (maximum[0] - new_value[0]) * 1000 + (
        #     maximum[1] - new_value[1]
        # )
        if new_value > maximum:
            if new_value > general_maximum:
                general_maximum = new_value
                general_position = new_position
                stalled = -1
            position = new_position
            maximum = new_value
        else:
            if random.random() < math.exp(-delta_e / temperature):
                maximum = new_value
                position = new_position

        stalled += 1

        if stalled > 10000:
            print(
                general_maximum,
                general_position,
                temperature,
                maximum,
                position,
            )
            maximum = general_maximum
            position = general_position
            stalled = 0
            temperature *= 0.99

        if temperature < 0.1:
            temperature = temperature_init

    return (
        -general_maximum[0],
        general_maximum,
        general_position,
        temperature,
        distance(general_position, (0, 0, 0)),
    )


def part2_alt(data):
    bots = convert_to_nanobots(data)
    xs = [x[0][0] for x in bots]
    ys = [x[0][1] for x in bots]
    zs = [x[0][2] for x in bots]

    dist = 1
    while dist < max(xs) - min(xs):
        dist *= 2

    while True:
        target_count = -1
        best = None
        best_val = None
        for x in range(min(xs), max(xs) + 1, dist):
            for y in range(min(ys), max(ys) + 1, dist):
                for z in range(min(zs), max(zs) + 1, dist):
                    count = 0
                    for (bx, by, bz), bdist in bots:
                        calc = abs(x - bx) + abs(y - by) + abs(z - bz)
                        if (calc - bdist) / dist <= 0:
                            count += 1
                    if count > target_count:
                        target_count = count
                        best_val = abs(x) + abs(y) + abs(z)
                        best = (x, y, z)
                    elif count == target_count:
                        if abs(x) + abs(y) + abs(z) < best_val:
                            best_val = abs(x) + abs(y) + abs(z)
                            best = (x, y, z)

        if dist == 1:
            break
        else:
            xs = [best[0] - dist, best[0] + dist]
            ys = [best[1] - dist, best[1] + dist]
            zs = [best[2] - dist, best[2] + dist]
            dist //= 2
    return best_val


if __name__ == '__main__':
    data_example = data_import('data/day23_example', str, ',')
    data = data_import('data/day23', str, ',')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data_example))
    print('Solution of 2 is', part2(data))

# > 40936474
# 40928110
# 882
# 43993035 - 910
# 43986891
# 43959619
# 43931045
# 43899897

# (909, -43028803) (18135641, 10669199, 14223963) 53090.554295511276 (38, -144354645) (48092285, 29460935, -66801425)
