from utils import data_import


def part1(data):
    return sum(max(item) - min(item) for item in data)


def part2(data):
    total = 0
    for item in data:
        for a in item:
            for b in item:
                if a != b and a / b == a // b:
                    total += a // b

    return total


if __name__ == '__main__':
    data = data_import('data/y2017/day2')
    data = [[int(d) for d in item.split()] for item in data]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
