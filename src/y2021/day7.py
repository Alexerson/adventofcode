from src.utils import data_import


def part1(data: list[int]) -> int:
    return min(
        sum(abs(x - position) for x in data)
        for position in range(min(data), max(data))
    )


def cost(x, y):
    n = abs(x - y)
    return n * (n + 1) // 2


def part2(data: list[int]) -> int:
    return min(
        sum(cost(x, position) for x in data)
        for position in range(min(data), max(data))
    )


if __name__ == '__main__':
    mydata = data_import('data/y2021/day7_example', split_char=',', cast=int)[
        0
    ]
    mydata = data_import('data/y2021/day7', split_char=',', cast=int)[0]

    print('Input is', mydata)

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
