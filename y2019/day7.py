from utils import data_import
from intcode import Program

from itertools import permutations

def part1(data):

    outputs = {}

    for settings in permutations(range(5), 5):
        input_ = 0
        for setting in settings:
            inputs = [setting, input_]
            input_ = list(Program(data).execute(inputs))[0]
        outputs[settings] = input_
    return max(outputs.items(), key=lambda a: a[1])


def part2(data):
    outputs = {}

    for settings in permutations(range(5, 10), 5):
        program_a, program_b, program_c, program_d, program_e = [Program(data) for _ in range(5)]

        setting_a, setting_b, setting_c, setting_d, setting_e = settings
        inputs_a = [setting_a, 0]
        inputs_b = [setting_b]
        inputs_c = [setting_c]
        inputs_d = [setting_d]
        inputs_e = [setting_e]

        while not all(program.finished for program in [program_a, program_b, program_c, program_d, program_e]):

            try:
                for out in program_a.execute(inputs_a):
                    inputs_b.append(out)
            except IndexError:
                pass

            try:
                for out in program_b.execute(inputs_b):
                    inputs_c.append(out)
            except IndexError:
                pass

            try:
                for out in program_c.execute(inputs_c):
                    inputs_d.append(out)
            except IndexError:
                pass

            try:
                for out in program_d.execute(inputs_d):
                    inputs_e.append(out)
            except IndexError:
                pass

            try:
                for out in program_e.execute(inputs_e):
                    inputs_a.append(out)
            except IndexError:
                pass

        outputs[settings] = out

    return max(outputs.items(), key=lambda a: a[1])

if __name__ == '__main__':

    print('Solution of example 1 is', part1([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]))
    print('Solution of example 2 is', part2([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]))

    data = data_import('y2019/data/day7', cast=int, split_char=',')[0]
    # print('Input is', data)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
 