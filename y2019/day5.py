from utils import data_import
from intcode import Program



def part1(data):
    program = Program(data)
    inputs = [1]
    outputs = []
    while not program.finished:
        outputs.append(program.run_until_output(inputs))
    return outputs[-2]

def part2(data):
    return Program(data).run_until_output([5])

if __name__ == '__main__':
    data = data_import('y2019/data/day5', cast=int, split_char=',')[0]
    # print('Input is', data)

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
