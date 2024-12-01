from utils import data_import
from y2017.day10 import part2 as knot_hash
from y2017.day10_alt import solve2 as knot_hash_alt


def part1(data):
    output = []
    for i in range(128):
        input_ = '{}-{}'.format(data, i)

        binary_hash = bin(int(knot_hash(input_), 16))[2:]

        output.append(binary_hash.zfill(128))
    return sum(d == '1' for line in output for d in line)


def find_region(coord, output):
    to_visit = set([coord])
    visited = set()
    match = set()

    while len(to_visit):
        cell = to_visit.pop()

        visited.add(cell)

        if output[cell[0]][cell[1]]:
            match.add(cell)
        else:
            continue

        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_cell = (cell[0] + i, cell[1] + j)
            if (
                new_cell[0] < 0
                or new_cell[1] < 0
                or new_cell[0] > 127
                or new_cell[1] > 127
                or new_cell in visited
            ):
                continue
            to_visit.add(new_cell)

    return match


def part2(data):
    output = []
    for i in range(128):
        input_ = '{}-{}'.format(data, i)

        binary_hash = bin(int(knot_hash(input_), 16))[2:].zfill(128)
        output.append([d == '1' for d in binary_hash.zfill(128)])

    regions = {}

    region_count = 0

    for line_i, line in enumerate(output):
        for column_i, cell in enumerate(line):
            if cell and (line_i, column_i) not in regions.keys():
                region = find_region((line_i, column_i), output)
                region_count += 1

                for i, j in region:
                    regions[(i, j)] = region_count

    return region_count


def show_regions(regions):
    for i in range(8):
        print(
            ''.join(str(regions.get((i, j), '..')).zfill(2) for j in range(8))
        )


if __name__ == '__main__':
    input_example = 'flqrgnkx'
    print('Solution of 1 is', part1(input_example))
    print('Solution of 2 is', part2(input_example))

    data = 'hwlqcszp'
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
