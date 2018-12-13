from utils import data_import


def part1(data):

    new_data = data.copy()

    current_position = 0
    step = 0

    while True:
        try:
            next_position = current_position + new_data[current_position]
        except IndexError:
            return step
        new_data[current_position] += 1
        step += 1
        current_position = next_position


def part2(data):
    new_data = data.copy()

    current_position = 0
    step = 0

    while True:
        try:
            offset = new_data[current_position]
            next_position = current_position + offset
        except IndexError:
            return step
        if offset >= 3:
            new_data[current_position] -= 1
        else:
            new_data[current_position] += 1
        step += 1
        current_position = next_position


if __name__ == '__main__':
    data = data_import('2017/data/day5', int)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
