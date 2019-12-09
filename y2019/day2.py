from utils import data_import
from intcode import Program



def part1(data):
    data = list(data)
    data[1] = 12
    data[2] = 2
    program = Program(data)
    list(program.execute())
    return program.memory[0]


def part2(data, output):
    for noun in range(100):
        for verb in range(100):
            memory = list(data)
            memory[1] = noun
            memory[2] = verb 
            program = Program(memory)
            list(program.execute())
            if program.memory[0] == output:
                return noun * 100 + verb


if __name__ == '__main__':
    data = data_import('y2019/data/day2', cast=int, split_char=',')[0]
    print('Input is', data)

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data, 19690720))