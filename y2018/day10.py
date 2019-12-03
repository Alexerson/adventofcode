import parse

from utils import data_import


def extract_data(data):

    format_string = "position=<{},{}> velocity=<{},{}>"
    out = [parse.parse(format_string, item) for item in data]

    return [[int(a) for a in line] for line in out]


def move_once(data):
    for item in data:
        item[0] += item[2]
        item[1] += item[3]

    return data


def move_back(data):
    for item in data:
        item[0] -= item[2]
        item[1] -= item[3]

    return data


def display_data(data, show=True):
    points = {}

    for item in data:
        points[(item[0], item[1])] = True

    x, y = zip(*points.keys())

    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)

    if show:
        for j in range(min_y, max_y + 1):
            line = []
            for i in range(min_x, max_x + 1):
                if points.get((i, j)):
                    line.append('#')
                else:
                    line.append('.')
            print(''.join(line))

    return points, min_x, max_x, min_y, max_y


def part1(data):

    time = 0

    data_ = extract_data(data)

    points, min_x, max_x, min_y, max_y = display_data(data_, False)
    distance = max_x - min_x + max_y - min_y

    while True:
        time += 1
        move_once(data_)

        points, min_x, max_x, min_y, max_y = display_data(data_, False)
        new_distance = max_x - min_x + max_y - min_y

        if new_distance > distance:
            break

        distance = new_distance

    move_back(data_)
    display_data(data_)

    return time - 1


if __name__ == '__main__':
    data = data_import('data/day10_example', str)
    print('Example:')
    print('Solution is', part1(data))

    print('Real:')
    data = data_import('data/day10_real', str)
    print('Solution is', part1(data))
