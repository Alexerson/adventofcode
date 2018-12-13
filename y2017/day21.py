import math

from utils import data_import


def flip(drawing):
    lines = drawing.split('/')
    return '/'.join(line[::-1] for line in lines)
    return drawing


def rotate(drawing):
    lines = drawing.split('/')
    size = len(lines)
    out = []
    for i in range(size):
        line = ""
        for j in range(size):
            line += lines[size - j - 1][i]
        out.append(line)

    return '/'.join(out)


def slice_drawing(drawing):
    lines = drawing.split('/')

    size = len(lines)

    if size % 2 == 0:
        subsize = 2
    else:
        subsize = 3

    pieces = []
    for piece_y in range(size // subsize):
        for piece_x in range(size // subsize):
            piece = []
            for j in range(subsize):
                for i in range(subsize):
                    piece.append(
                        lines[piece_y * subsize + j][piece_x * subsize + i]
                    )
                piece.append("/")
            pieces.append(''.join(piece[:-1]))
    return pieces


def merge_drawing(pieces):
    size = int(math.sqrt(sum(bit != '/' for piece in pieces for bit in piece)))
    out = [''] * size
    line_index = 0
    col_index = 0
    for piece in pieces:
        for index, line in enumerate(piece.split("/")):
            out[index + line_index] += line
        col_index += len(piece.split("/"))
        if col_index >= size:
            line_index += len(piece.split("/"))
            col_index = 0

    return '/'.join(out)


def show_drawing(drawing):
    print(drawing.replace('/', '\n'))


def convert_data_to_rules(data):
    rules = {}

    for line in data:
        current = line[0]
        output = line[2]

        # 1
        rules[current] = output
        rules[flip(current)] = output

        # 2
        current = rotate(current)
        rules[current] = output
        rules[flip(current)] = output

        # 3
        current = rotate(current)
        rules[current] = output
        rules[flip(current)] = output

        # 4
        current = rotate(current)
        rules[current] = output
        rules[flip(current)] = output

    return rules


def apply_rules(drawing, rules):
    return merge_drawing([rules[s] for s in slice_drawing(drawing)])


def part1(data, iterations=5):

    rules = convert_data_to_rules(data)

    drawing = '.#./..#/###'

    for iteration in range(iterations):
        drawing = apply_rules(drawing, rules)

    return sum(bit == '#' for bit in drawing)


def part2(data):
    return part1(data, iterations=18)


if __name__ == '__main__':
    data = data_import('2017/data/day21_example', str, True)
    print('Solution of 1 is', part1(data, 2))
    print('Solution of 2 is', part2(data))

    data = data_import('2017/data/day21_real', str, True)
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
