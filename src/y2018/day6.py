import collections

from utils import data_import


# Manathan distance
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part1(data):

    # We don't need to test anything, just start with min and max
    min_x = min(list(zip(*data))[0])
    min_y = min(list(zip(*data))[1])
    max_x = max(list(zip(*data))[0])
    max_y = max(list(zip(*data))[1])

    repartition = {}

    # Bruteforce: we check for each point which is closer
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):

            minimum = None
            index_min = None

            for index, point in enumerate(data):
                dist = distance((i, j), point)
                if minimum is None:
                    minimum = dist
                    index_min = index

                else:

                    if dist < minimum:
                        minimum = dist
                        index_min = index
                    elif dist == minimum:
                        index_min = '.'

            repartition[(i, j)] = index_min

    # We exclude edges, those are infinite boundaries
    exclusions = set(['.'])
    for i in range(min_x, max_x):
        exclusions.add(repartition[(i, min_y)])
        exclusions.add(repartition[(i, max_y)])
    for j in range(min_y, max_y):
        exclusions.add(repartition[(min_x, j)])
        exclusions.add(repartition[(max_x, j)])

    # We count
    counter = collections.Counter(
        item for item in repartition.values() if item not in exclusions
    )

    return counter.most_common(1)[0][1]


def part2(data, limit=10000):
    # We don't need to test anything, just start with min and max
    min_x = min(list(zip(*data))[0])
    min_y = min(list(zip(*data))[1])
    max_x = max(list(zip(*data))[0])
    max_y = max(list(zip(*data))[1])

    distances = {}

    # Bruteforce: we check for each point which is closer
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):

            distances[(i, j)] = sum(distance((i, j), point) for point in data)

    return sum(dist < limit for dist in distances.values())


if __name__ == '__main__':
    data = data_import('data/day6')
    data = [item.split(', ') for item in data]
    data = [(int(a), int(b)) for a, b in data]

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
