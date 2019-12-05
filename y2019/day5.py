from utils import data_import
from intcode import execute



def part1(data):
    data = list(data)
    return execute(data, [1])[1][-1]

def part2(data):
    data = list(data)
    return execute(data, [5])[1][0]

if __name__ == '__main__':
    data = data_import('y2019/data/day5', cast=int, split_char=',')[0]
    print('Input is', data)

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
