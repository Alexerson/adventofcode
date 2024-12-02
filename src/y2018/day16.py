from utils import data_import

functions = {
    'addr': lambda a, b, registers: registers[a] + registers[b],
    'addi': lambda a, b, registers: registers[a] + b,
    'mulr': lambda a, b, registers: registers[a] * registers[b],
    'muli': lambda a, b, registers: registers[a] * b,
    'banr': lambda a, b, registers: registers[a] & registers[b],
    'bani': lambda a, b, registers: registers[a] & b,
    'borr': lambda a, b, registers: registers[a] | registers[b],
    'bori': lambda a, b, registers: registers[a] | b,
    'setr': lambda a, _b, registers: registers[a],
    'seti': lambda a, _b, _registers: a,
    'gtir': lambda a, b, registers: int(a > registers[b]),
    'gtri': lambda a, b, registers: int(registers[a] > b),
    'gtrr': lambda a, b, registers: int(registers[a] > registers[b]),
    'eqir': lambda a, b, registers: int(a == registers[b]),
    'eqri': lambda a, b, registers: int(registers[a] == b),
    'eqrr': lambda a, b, registers: int(registers[a] == registers[b]),
}


def split_data(data):
    line_no = 0
    instructions = []
    tests = []

    while line_no < len(data):
        if data[line_no].startswith('Before'):
            before = [int(b) for b in data[line_no][9:-1].split(',')]
            command = [int(b) for b in data[line_no + 1].split(' ')]
            after = [int(b) for b in data[line_no + 2][9:-1].split(',')]

            instructions.append((before, command, after))
            line_no += 3
        else:
            command = [int(b) for b in data[line_no].split(' ')]
            tests.append(command)
            line_no += 1

    return instructions, tests


def part1(data):
    instructions, _ = split_data(data)

    more_than_3 = 0

    for before, command, after in instructions:
        correct = 0
        _opcode, a, b, c = command
        for func in functions.values():
            correct += after[c] == func(a, b, before)
        more_than_3 += correct >= 3

    return more_than_3


def find_functions_mapping(instructions):
    mapping = {}

    for func_name, func in functions.items():
        possibles = set(range(16))

        for before, command, after in instructions:
            opcode, a, b, c = command

            if opcode not in possibles:
                continue

            if after[c] != func(a, b, before):
                possibles.remove(opcode)

        mapping[func_name] = possibles

    final_mapping = {}

    while len(final_mapping) < 16:
        for func_name, possibles in mapping.items():
            not_assigned = [
                poss for poss in possibles if poss not in final_mapping
            ]
            if len(not_assigned) == 1:
                final_mapping[not_assigned[0]] = func_name

    return final_mapping


def part2(data):
    instructions, program = split_data(data)

    functions_mapping = find_functions_mapping(instructions)

    registers = [0] * 4

    for command in program:
        opcode, a, b, c = command
        func_name = functions_mapping[opcode]
        registers[c] = functions[func_name](a, b, registers)

    return registers[0]


if __name__ == '__main__':
    data = data_import('data/day16', str)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
