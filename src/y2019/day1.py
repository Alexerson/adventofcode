from src.utils import data_import


def compute_fuel(module):
    return max(int(module / 3) - 2, 0)


def compute_fuel_with_extra(module):
    fuel = compute_fuel(module)
    total = fuel
    while fuel > 0:
        fuel = compute_fuel(fuel)
        total += fuel

    return total


def part1(data):
    return sum(compute_fuel(item) for item in data)


def part2(data):
    return sum(compute_fuel_with_extra(item) for item in data)


if __name__ == '__main__':
    data = data_import('data/y2019/day1', int)
    print('Input is', data)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
