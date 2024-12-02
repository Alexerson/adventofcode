import contextlib
import operator
from itertools import permutations

from intcode import Program

from utils import data_import


def part1(data):
    outputs = {}

    for settings in permutations(range(5), 5):
        input_ = 0
        for setting in settings:
            inputs = [setting, input_]
            input_ = Program(data).run_until_output(inputs)
        outputs[settings] = input_
    return max(outputs.items(), key=operator.itemgetter(1))


def part2(data):
    outputs = {}

    for settings in permutations(range(5, 10), 5):
        program_a, program_b, program_c, program_d, program_e = [
            Program(data) for _ in range(5)
        ]

        setting_a, setting_b, setting_c, setting_d, setting_e = settings
        inputs_a = [setting_a, 0]
        inputs_b = [setting_b]
        inputs_c = [setting_c]
        inputs_d = [setting_d]
        inputs_e = [setting_e]

        while not all(
            program.finished
            for program in [
                program_a,
                program_b,
                program_c,
                program_d,
                program_e,
            ]
        ):
            with contextlib.suppress(IndexError):
                inputs_b.append(program_a.run_until_output(inputs_a))

            with contextlib.suppress(IndexError):
                inputs_c.append(program_b.run_until_output(inputs_b))

            with contextlib.suppress(IndexError):
                inputs_d.append(program_c.run_until_output(inputs_c))

            with contextlib.suppress(IndexError):
                inputs_e.append(program_d.run_until_output(inputs_d))

            with contextlib.suppress(IndexError):
                inputs_a.append(program_e.run_until_output(inputs_e))

        outputs[settings] = inputs_a[-2]

    return max(outputs.items(), key=operator.itemgetter(1))


if __name__ == '__main__':
    print(
        'Solution of example 1 is',
        part1([
            3,
            15,
            3,
            16,
            1002,
            16,
            10,
            16,
            1,
            16,
            15,
            15,
            4,
            15,
            99,
            0,
            0,
        ]),
    )
    print(
        'Solution of example 2 is',
        part2(
            [
                3,
                26,
                1001,
                26,
                -4,
                26,
                3,
                27,
                1002,
                27,
                2,
                27,
                1,
                27,
                26,
                27,
                4,
                27,
                1001,
                28,
                -1,
                28,
                1005,
                28,
                6,
                99,
                0,
                0,
                5,
            ],
        ),
    )

    data = data_import('data/y2019/day7', cast=int, split_char=',')[0]
    # print('Input is', data)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
