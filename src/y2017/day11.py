from src.utils import data_import


def distance(point):
    if point[0] == 0 or point[1] == 0:
        return abs(point[1]) + abs(point[0])

    if point[0] > 0 and point[1] < 0:
        return point[0] - point[1]

    if point[0] < 0 and point[1] > 0:
        return point[1] - point[0]

    if point[0] > 0 and point[1] > 0:
        return max(point[0], point[1])

    if point[0] < 0 and point[1] < 0:
        return -min(point[0], point[1])
    return None


def parts(data):
    position = [0, 0]
    max_distance = 0

    for item in data:
        if item == 'n':
            position[1] += 1
        elif item == 'ne':
            position[0] += 1
            position[1] += 1
        elif item == 'se':
            position[0] += 1
        elif item == 's':
            position[1] += -1
        elif item == 'sw':
            position[0] += -1
            position[1] += -1
        elif item == 'nw':
            position[0] += -1

        dist = distance(position)
        max_distance = max(dist, max_distance)

    return distance(position), max_distance


if __name__ == '__main__':
    data = data_import('data/y2017/day11', str, ',')[0]

    part1, part2 = parts(data)

    print('Solution of 1 is', part1)
    print('Solution of 2 is', part2)
