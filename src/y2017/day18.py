from collections import deque

from utils import data_import


def part1(data):
    registers = {}

    index = 0
    sound = None

    while True:
        command = data[index]

        if command[0] in ('snd', 'rcv', 'jgz'):
            try:
                value1 = int(command[1])
            except ValueError:
                value1 = registers.get(command[1], 0)

        if command[0] in ('set', 'add', 'mul', 'mod', 'jgz'):
            try:
                value2 = int(command[2])
            except ValueError:
                value2 = registers.get(command[2], 0)

        if command[0] == 'snd':
            sound = value1

        elif command[0] == 'set':
            registers[command[1]] = value2

        elif command[0] == 'add':
            registers[command[1]] = registers.get(command[1], 0) + value2

        elif command[0] == 'mul':
            registers[command[1]] = registers.get(command[1], 0) * value2

        elif command[0] == 'mod':
            registers[command[1]] = registers.get(command[1], 0) % value2

        elif command[0] == 'rcv':
            if value1 != 0:
                return sound

        elif command[0] == 'jgz':
            if value1 > 0:
                index += value2 - 1

        index += 1


class Program:
    index = 0
    started = False

    def __init__(self, value, data):
        self.registers = {}
        self.registers['p'] = value
        self.queue = deque([])
        self.data = data

    def push(self, value):
        self.queue.append(value)

    def pull(self):
        return self.queue.popleft()

    def run_until_blocked(self, other_program):

        self.started = True
        sent = 0

        while True:
            try:
                command = self.data[self.index]
            except IndexError:
                return sent

            if command[0] in ('snd', 'jgz'):
                try:
                    value1 = int(command[1])
                except ValueError:
                    value1 = self.registers.get(command[1], 0)

            if command[0] in ('set', 'add', 'mul', 'mod', 'jgz'):
                try:
                    value2 = int(command[2])
                except ValueError:
                    value2 = self.registers.get(command[2], 0)

            if command[0] == 'snd':
                other_program.push(value1)
                sent += 1

            elif command[0] == 'set':
                self.registers[command[1]] = value2

            elif command[0] == 'add':
                self.registers[command[1]] = (
                    self.registers.get(command[1], 0) + value2
                )

            elif command[0] == 'mul':
                self.registers[command[1]] = (
                    self.registers.get(command[1], 0) * value2
                )

            elif command[0] == 'mod':
                self.registers[command[1]] = (
                    self.registers.get(command[1], 0) % value2
                )

            elif command[0] == 'rcv':
                try:
                    self.registers[command[1]] = self.pull()
                except IndexError:
                    return sent

            elif command[0] == 'jgz':
                if value1 > 0:
                    self.index += value2 - 1

            self.index += 1

    def is_locked(self):
        return self.started and not self.queue


def part2(data):
    program0 = Program(0, data)
    program1 = Program(1, data)

    sent = 0

    while not program0.is_locked() or not program1.is_locked():
        program0.run_until_blocked(program1)
        sent += program1.run_until_blocked(program0)

    return sent


if __name__ == '__main__':
    data_example = data_import('data/y2017/day18_example', str, ' ')
    print('Solution of 1 is', part1(data_example))
    data_example2 = data_import('data/y2017/day18_example2', str, ' ')
    print('Solution of 2 is', part2(data_example2))

    data_real = data_import('data/y2017/day18_real', str, ' ')
    print('Solution of 1 is', part1(data_real))
    print('Solution of 2 is', part2(data_real))
