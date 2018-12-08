from utils import data_import


def eval_condition(condition, v1, v2):
    if condition == '>':
        return v1 > v2
    if condition == '<':
        return v1 < v2
    if condition == '>=':
        return v1 >= v2
    if condition == '<=':
        return v1 <= v2
    if condition == '==':
        return v1 == v2
    if condition == '!=':
        return v1 != v2


def parts(data):

    registers = {}
    max_ever = 0

    for item in data:
        variable = item[0]
        if variable not in registers:
            registers[variable] = 0
        increment = item[1] == 'inc' and 1 or -1
        value = int(item[2])

        condition_variable = item[4]
        condition = item[5]
        condition_value = int(item[6])

        if eval_condition(
            condition, registers.get(condition_variable, 0), condition_value
        ):
            registers[variable] += increment * value

            if registers[variable] > max_ever:
                max_ever = registers[variable]

    return max(registers.values()), max_ever


def part1(data):
    return parts(data)[0]


def part2(data):
    return parts(data)[1]


if __name__ == '__main__':
    data = data_import('2017/data/day8_real', str, True)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
