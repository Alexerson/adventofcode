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


def part1(data, registers=None, one_loop=False):
    if registers is None:
        registers = [0] * 6

    line = data[0]
    instruction_register = int(line[1])

    data = data[1:]

    while True:
        instruction_pointer = registers[instruction_register]
        if one_loop and instruction_pointer == 2:
            return registers
        try:
            line = data[instruction_pointer]
        except IndexError:
            return registers[0]

        command = line[0]
        a = int(line[1])
        b = int(line[2])
        register_id = int(line[3])

        registers[register_id] = functions[command](a, b, registers)

        registers[instruction_register] += 1


def part2(data):
    # This has to be done manually.
    # Running manually, we notice that there is 2 loops one in the other.
    # Equivalent is:
    # Run the "intro" and when you enter the loop,
    # find all the divisors of R3 (in my case it's R3)
    # R0 will be the sum of all divisors of r3

    # Rune once and stop when we enter the loop
    registers = part1(data, [1, 0, 0, 0, 0, 0], one_loop=True)

    number = max(registers)

    total = 0
    for nb in range(1, number + 1):
        if number % nb == 0:
            total += nb

    return total


if __name__ == '__main__':
    data_example = data_import('data/day19_example', str, ' ')
    data_real = data_import('data/day19_real', str, ' ')
    print('Solution of 1 is', part1(data_example))
    print('Solution of 1 is', part1(data_real))
    print('Solution of 2 is', part2(data_real))
