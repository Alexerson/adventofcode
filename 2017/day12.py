from utils import data_import


def build_mappings(data):
    mappings = {}

    for origin, destinations in data:
        origin = int(origin)
        if origin not in mappings:
            mappings[origin] = []
        for dest in destinations.split(','):
            mappings[origin].append(int(dest.strip()))

    return mappings


def part1(data):
    mappings = build_mappings(data)

    known = set()

    to_visit = [0]

    while to_visit:
        node = to_visit.pop()
        known.add(node)
        for dest in mappings.get(node):
            if dest not in known:
                to_visit.append(dest)

    return known


def part2(data):
    mappings = build_mappings(data)

    unknown = set(mappings.keys())

    groups = 0

    while unknown:
        groups += 1
        to_visit = [unknown.pop()]

        while to_visit:
            node = to_visit.pop()
            if node in unknown:
                unknown.remove(node)
            for dest in mappings.get(node):
                if dest in unknown:
                    to_visit.append(dest)

    return groups


if __name__ == '__main__':
    data = data_import('2017/data/day12_example', str, '<->')

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))

    data = data_import('2017/data/day12_real', str, '<->')

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
