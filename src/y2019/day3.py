from utils import data_import


def build_path(data):
    path = {}
    current = [0, 0]
    steps = 0

    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    for branch in data:
        direction = branch[0]
        distance = int(branch[1:])

        diff = directions[direction]

        for i in range(distance):
            if tuple(current) not in path:
                path[tuple(current)] = steps
            current[0] += diff[0]
            current[1] += diff[1]
            steps += 1

    return path


def part1(data):
    # We build the paths
    path1 = build_path(data[0])
    path2 = build_path(data[1])

    # We find the intersections = cells in both paths
    intersections = set(path1.keys()) & set(path2.keys())

    # 0,0 is ignored
    intersections.remove((0, 0))

    # We want the minimum manathan distance
    return min(abs(a) + abs(b) for a, b in intersections)


def part2(data, output):
    # We build the paths
    path1 = build_path(data[0])
    path2 = build_path(data[1])

    # We find the intersections = cells in both paths
    intersections = set(path1.keys()) & set(path2.keys())

    # 0,0 is ignored
    intersections.remove((0, 0))

    # We want the minimum total of steps
    return min(path1.get(point) + path2.get(point) for point in intersections)


if __name__ == '__main__':
    data = data_import('data/y2019/day3', cast=str, split_char=',')
    print('Input is', data)

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data, 19690720))
