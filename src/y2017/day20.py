import collections
import operator

from src.utils import data_import


def convert(data):
    particules = []
    for p, v, a in data:
        p = p[3:-1].split(',')
        v = v[3:-1].split(',')
        a = a[3:-1].split(',')

        particules.append(
            ([int(v) for v in p], [int(v) for v in v], [int(v) for v in a]),
        )
    return particules


def move_particule(particule):
    particule[1][0] += particule[2][0]
    particule[1][1] += particule[2][1]
    particule[1][2] += particule[2][2]
    particule[0][0] += particule[1][0]
    particule[0][1] += particule[1][1]
    particule[0][2] += particule[1][2]


def part1(data, loops=100000000):
    particules = convert(data)

    velocities = [
        abs(particule[2][0] * loops + particule[1][0])
        + abs(particule[2][1] * loops + particule[1][1])
        + abs(particule[2][2] * loops + particule[1][2])
        for particule in particules
    ]

    return min(
        ((index, value) for index, value in enumerate(velocities)),
        key=operator.itemgetter(1),
    )[0]


def part2(data, loops=1000):
    particules = convert(data)

    i = 0
    for i in range(loops):
        # while True:
        i += 1
        for particule in particules:
            move_particule(particule)

        counter = collections.Counter(
            tuple(particule[0]) for particule in particules
        )

        collisions = {
            position for position, count in counter.items() if count > 1
        }

        if collisions:
            particules = [
                particule
                for particule in particules
                if tuple(particule[0]) not in collisions
            ]

    return len(particules)


if __name__ == '__main__':
    data = data_import('data/y2017/day20', str, ', ')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
