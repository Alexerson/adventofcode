from src.utils import data_import


def part1(data: list[int]) -> int:
    previous = data[0]
    total = 0
    for current in data[1:]:
        if current > previous:
            total += 1
        previous = current
    return total


def part2(data: list[int]) -> int:
    total = 0
    a, b, c = data[:3]
    previous = a + b + c

    for i in data[3:]:
        a, b, c = b, c, i
        current = a + b + c
        if current > previous:
            total += 1
        previous = current
    return total


if __name__ == '__main__':
    mydata = data_import('data/y2021/day1', int)
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
