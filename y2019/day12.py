import collections
import itertools
import math
from functools import lru_cache

from intcode import Program

from utils import data_import


@lru_cache
def get_prime_factors(number):
    for i in range(2, number):
        if number % i == 0:
            return [i] + get_prime_factors(number // i)

    return [number]


def lcm(*numbers):
    factors = {}

    for number in numbers:
        prime_factors = get_prime_factors(number)

        for value, count in collections.Counter(prime_factors).items():
            if factors.get(value, 0) < count:
                factors[value] = count

    number = 1

    for value, count in factors.items():
        number *= value ** count

    return number


class Moon(object):
    def __init__(self, label, x, y, z):

        self.label = label

        self.x = x
        self.y = y
        self.z = z

        self.vx = 0
        self.vy = 0
        self.vz = 0

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def get_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    def __str__(self):
        return f'Moon {self.label} <{self.x}, {self.y}, {self.z}> <{self.vx}, {self.vy}, {self.vz}>'

    def get_status(self):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz)


def part1(moons, steps=1000):

    for step in range(steps):
        for moon1, moon2 in itertools.combinations(moons, 2):
            if moon1.x > moon2.x:
                moon1.vx -= 1
                moon2.vx += 1
            elif moon1.x < moon2.x:
                moon1.vx += 1
                moon2.vx -= 1

            if moon1.y > moon2.y:
                moon1.vy -= 1
                moon2.vy += 1
            elif moon1.y < moon2.y:
                moon1.vy += 1
                moon2.vy -= 1

            if moon1.z > moon2.z:
                moon1.vz -= 1
                moon2.vz += 1
            elif moon1.z < moon2.z:
                moon1.vz += 1
                moon2.vz -= 1

        for moon in moons:
            moon.x += moon.vx
            moon.y += moon.vy
            moon.z += moon.vz

    return sum(moon.get_energy() for moon in moons)


def part2(moons):

    step = 0
    positions_x = sum(((moon.x, moon.vx) for moon in moons), start=())
    positions_y = sum(((moon.y, moon.vy) for moon in moons), start=())
    positions_z = sum(((moon.z, moon.vz) for moon in moons), start=())
    history_x = {positions_x: step}
    history_y = {positions_y: step}
    history_z = {positions_z: step}

    period_x = None
    period_y = None
    period_z = None

    while period_x is None or period_y is None or period_z is None:
        step += 1
        for moon1, moon2 in itertools.combinations(moons, 2):
            if moon1.x > moon2.x:
                moon1.vx -= 1
                moon2.vx += 1
            elif moon1.x < moon2.x:
                moon1.vx += 1
                moon2.vx -= 1

            if moon1.y > moon2.y:
                moon1.vy -= 1
                moon2.vy += 1
            elif moon1.y < moon2.y:
                moon1.vy += 1
                moon2.vy -= 1

            if moon1.z > moon2.z:
                moon1.vz -= 1
                moon2.vz += 1
            elif moon1.z < moon2.z:
                moon1.vz += 1
                moon2.vz -= 1

        for moon in moons:
            moon.x += moon.vx
            moon.y += moon.vy
            moon.z += moon.vz

            status = moon.get_status()

        positions_x = sum(((moon.x, moon.vx) for moon in moons), start=())
        positions_y = sum(((moon.y, moon.vy) for moon in moons), start=())
        positions_z = sum(((moon.z, moon.vz) for moon in moons), start=())

        if period_x is None and positions_x in history_x:
            period_x = step - history_x[positions_x]

        if period_y is None and positions_y in history_y:
            period_y = step - history_y[positions_y]

        if period_z is None and positions_z in history_z:
            period_z = step - history_z[positions_z]

        history_x[positions_x] = step
        history_y[positions_y] = step
        history_z[positions_z] = step

    return lcm(period_x, period_y, period_z)


if __name__ == '__main__':

    moons = [
        Moon(1, -1, 0, 2),
        Moon(2, 2, -10, -7),
        Moon(3, 4, -8, 8),
        Moon(4, 3, 5, -1),
    ]
    print('Solution of 2 is', part2(moons))

    moons = [
        Moon(1, -8, -10, 0),
        Moon(2, 5, 5, 10),
        Moon(3, 2, -7, 3),
        Moon(4, 9, -8, -3),
    ]
    print('Solution of 1 is', part1(moons, 100))
    print('Solution of 2 is', part2(moons))

    moons = [
        Moon(1, 17, -12, 13),
        Moon(2, 2, 1, 1),
        Moon(3, -1, -17, 7),
        Moon(4, 12, -14, 18),
    ]

    print('Solution of 1 is', part1(moons, 1000))
    print('Solution of 2 is', part2(moons))
