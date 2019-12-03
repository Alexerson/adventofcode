from utils import data_import

functions = {
    "addr": lambda a, b, registers: registers[a] + registers[b],
    "addi": lambda a, b, registers: registers[a] + b,
    "mulr": lambda a, b, registers: registers[a] * registers[b],
    "muli": lambda a, b, registers: registers[a] * b,
    "banr": lambda a, b, registers: registers[a] & registers[b],
    "bani": lambda a, b, registers: registers[a] & b,
    "borr": lambda a, b, registers: registers[a] | registers[b],
    "bori": lambda a, b, registers: registers[a] | b,
    "setr": lambda a, b, registers: registers[a],
    "seti": lambda a, b, registers: a,
    "gtir": lambda a, b, registers: int(a > registers[b]),
    "gtri": lambda a, b, registers: int(registers[a] > b),
    "gtrr": lambda a, b, registers: int(registers[a] > registers[b]),
    "eqir": lambda a, b, registers: int(a == registers[b]),
    "eqri": lambda a, b, registers: int(registers[a] == b),
    "eqrr": lambda a, b, registers: int(registers[a] == registers[b]),
}


def part1(data):
    # We notice registers[0] is never used nor tampered with.
    # We simply need to find what is the value of R1
    # when the command 28 is ran for the first time
    registers = [0] * 6

    line = data[0]
    instruction_register = int(line[1])

    commands = data[1:]

    # while tuple(registers) not in known:
    while registers[instruction_register] != 28:
        instruction_pointer = registers[instruction_register]
        try:
            line = commands[instruction_pointer]
        except IndexError:
            raise

        command = line[0]
        a = int(line[1])
        b = int(line[2])
        register_id = int(line[3])

        if command == 'bani':
            pass

        registers[register_id] = functions[command](a, b, registers)

        registers[instruction_register] += 1

    return registers[1]


def part2(data):
    # We notice registers[0] is never used nor tampered with.
    # We simply need to find what is the value of R1
    # when the command 28 is ran for the first time

    # At some point we'll try a value for R1 we tried already.
    # In that case, the previous tried is the correct one!
    registers = [0] * 6

    line = data[0]
    instruction_register = int(line[1])

    commands = data[1:]

    known = set()
    last_valid = None

    while registers[instruction_register] != 28 or registers[1] not in known:
        if registers[instruction_register] == 28:
            known.add(registers[1])
            last_valid = registers[1]

        instruction_pointer = registers[instruction_register]
        try:
            line = commands[instruction_pointer]
        except IndexError:
            raise
            # return registers[0]

        command = line[0]
        a = int(line[1])
        b = int(line[2])
        register_id = int(line[3])

        registers[register_id] = functions[command](a, b, registers)

        registers[instruction_register] += 1
        print(line, registers)

    return last_valid


def part2_improved():
    # We notice registers[0] is never used nor tampered with.
    # We simply need to find what is the value of R1
    # when the command 28 is ran for the first time

    # At some point we'll try a value for R1 we tried already.
    # In that case, the previous tried is the correct one!
    registers = [0, 3422393, 65536, 0, 18, 1]

    known = set()
    last_valid = None

    while True:

        pass

        if registers[1] in known:
            return last_valid

        known.add(registers[1])
        last_valid = registers[1]

    return last_valid


if __name__ == '__main__':
    data = data_import('data/day21', str, ' ')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
