from collections import deque
from string import ascii_lowercase

from src.utils import data_import


def part1(data, length=16, line=None):
    if line is None:
        line = deque(ascii_lowercase[:length])

    for move in data:
        if move[0] == 's':
            line.rotate(int(move[1:]))

        if move[0] == 'x':
            pos1, pos2 = move[1:].split('/')
            pos1 = int(pos1)
            pos2 = int(pos2)
            line[pos1], line[pos2] = line[pos2], line[pos1]

        if move[0] == 'p':
            prog1, prog2 = move[1:].split('/')
            pos1 = line.index(prog1)
            pos2 = line.index(prog2)
            line[pos1], line[pos2] = line[pos2], line[pos1]

    return ''.join(line)


def part2(data, length=16):
    line = deque(ascii_lowercase[:length])

    known = {}
    iteration = 0

    while ''.join(line) not in known:
        known[''.join(line)] = iteration
        part1(data, line=line)
        iteration += 1

    return {b: a for a, b in known.items()}[1000000000 % iteration]


if __name__ == '__main__':
    data_example = ['s1', 'x3/4', 'pe/b']
    data_real = data_import('data/y2017/day16', str, ',')[0]

    print('Solution of 1 is', part1(data_example, 5))
    print('Solution of 2 is', part2(data_example, 5))

    print('Solution of 1 is', part1(data_real))
    print('Solution of 2 is', part2(data_real))
