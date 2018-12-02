from utils import data_import


def part1(data):
    return sum(data)


def part2(data):

    known = [0]
    current = 0

    # Depending on the input, this can take a while (and even never finish)
    # With my input and machine, it takes about 3 minutes to end.
    while True:
        for item in data:
            current += item
            if current in known:
                return current
            else:
                known.append(current)


if __name__ == '__main__':
    data = data_import('data/day1', int)
    print('Input is', data)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
