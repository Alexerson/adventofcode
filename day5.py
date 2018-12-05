from utils import data_import


def is_reverse_polarity(a, b):
    return a.lower() == b.lower() and a != b


def remove_once(data):
    set_chars = set(list(data.lower()))

    for char in set_chars:
        data = data.replace('{}{}'.format(char, char.upper()), '')
        data = data.replace('{}{}'.format(char.upper(), char), '')

    return data


def part1(data):

    len_before = len(data)
    len_after = 0

    while len_before != len_after:
        len_before = len(data)
        data = remove_once(data)
        len_after = len(data)

    return data


def part2(data):
    set_chars = set(list(data.lower()))
    results = []

    for char in set_chars:

        reduced_data = data.replace(char, '').replace(char.upper(), '')
        result = len(part1(reduced_data))
        results.append((char, result))
    return min(results, key=lambda a: a[1])


if __name__ == '__main__':
    data = data_import('data/day5')[0]

    part1_result = part1(data)
    print('Solution of 1 is', len(part1_result))

    # It's easy to prove that part2(data) == part2(part1(data)) and
    # the latter is faster so no reason not to do it!
    print('Solution of 2 is', part2(part1_result))
