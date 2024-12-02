from collections import Counter

from src.utils import data_import


def part1(data, nb_cycles=10, debug=False):
    known = {}

    iterations = 0
    while '\n'.join(data) not in known:
        known['\n'.join(data)] = iterations
        iterations += 1
        new_data = []

        for line_no, line in enumerate(data):
            new_line = ''
            for col_no, cell in enumerate(line):
                neighbors = [
                    data[line_no + i][col_no + j]
                    for i in range(-1, 2)
                    for j in range(-1, 2)
                    if line_no + i >= 0
                    and line_no + i < len(data)
                    and col_no + j >= 0
                    and col_no + j < len(line)
                ]
                counter = Counter(neighbors)

                if cell == '.':
                    if counter['|'] >= 3:
                        new_line += '|'
                    else:
                        new_line += '.'

                elif cell == '|':
                    if counter['#'] >= 3:
                        new_line += '#'
                    else:
                        new_line += '|'

                elif cell == '#':
                    if counter['#'] >= 2 and counter['|'] >= 1:
                        new_line += '#'
                    else:
                        new_line += '.'
            new_data.append(new_line)

        data = new_data

        if debug:
            print(
                '\n'.join(data)
                .replace('.', '  ')
                .replace('#', '🌱')
                .replace('|', '🌳'),
            )
            print()

        if iterations == nb_cycles:
            counter = Counter(''.join(data))
            return counter['#'] * counter['|']

    period = iterations - known['\n'.join(data)]
    offset = iterations - period

    equivalent = (nb_cycles - offset) % period + offset

    known_reverse = {b: a for a, b in known.items()}

    counter = Counter(''.join(known_reverse[equivalent]))
    return period, offset, equivalent, counter['#'] * counter['|']


if __name__ == '__main__':
    data_example = data_import('data/day18_example', str)
    print('Solution of 1 is', part1(data_example))
    print('Solution of 2 is', part1(data_example, 1000000000))

    data_real = data_import('data/day18_real', str)
    print('Solution of 1 is', part1(data_real))
    print('Solution of 2 is', part1(data_real, 1000000000))
