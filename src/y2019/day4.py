from collections import Counter


def valid1(num):
    i = str(num)
    if sorted(i) != list(i):
        return False
    return any(j >= 2 for j in Counter(i).values())


def part1(start, end):
    return sum(1 for i in range(start, end) if valid1(i))


def valid2(num):
    i = str(num)
    if sorted(i) != list(i):
        return False
    return any(j == 2 for j in Counter(i).values())


def part2(start, end):
    return sum(1 for i in range(start, end) if valid2(i))


if __name__ == '__main__':
    start = 152085
    end = 670283
    print('Solution of 1 is', part1(start, end))
    print('Solution of 2 is', part2(start, end))
