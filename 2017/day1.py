from utils import data_import


def part1(data, step=1):
    return sum(
        value
        for index, value in enumerate(data)
        if value == data[(index + step) % len(data)]
    )


def part2(data):
    step = len(data) // 2

    return part1(data, step)


if __name__ == '__main__':
    data = data_import('2017/data/day1')
    data = [int(d) for d in data[0]]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
