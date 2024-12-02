from src.utils import data_import


def parts(data_):
    total = sum(data_)

    data = data_.copy()
    known = {}

    count = len(data)

    cycle = 0

    while tuple(data) not in known:
        known[(tuple(data))] = cycle
        cycle += 1
        bank, content = max(enumerate(data), key=lambda a: (a[1], -a[0]))

        data[bank] = 0
        increment = content // count
        rest = content % count

        for index in range(count):
            data[index] += increment

        min_bonus = bank + 1
        max_bonus = bank + rest

        for index in range(min_bonus, max_bonus + 1):
            data[index % count] += 1

        assert sum(data) == total

    return cycle, cycle - known[tuple(data)]


if __name__ == '__main__':
    data = data_import('data/y2017/day6', int, '\t', rstrip=True)[0]
    print(data)
    part1, part2 = parts(data)
    print('Solution of 1 is', part1)
    print('Solution of 2 is', part2)
