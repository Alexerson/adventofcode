from collections import deque

from utils import data_import


def part1(steps, max_range=2017):
    spinlock = deque([0])

    for i in range(1, max_range + 1):
        spinlock.rotate(-steps)
        spinlock.append(i)

    return spinlock.popleft()


def part2(steps, max_range=50000000):
    position = 0

    val_after_0 = 0

    for value in range(1, max_range + 1):
        position = (position + steps) % value + 1
        if position == 1:
            val_after_0 = value

    return val_after_0


if __name__ == '__main__':
    data_example = 3
    print('Solution of 1 is', part1(data_example))
    print('Solution of 2 is', part2(data_example))

    data_real = 304
    print('Solution of 1 is', part1(data_real))
    print('Solution of 2 is', part2(data_real))
