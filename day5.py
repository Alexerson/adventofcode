from utils import data_import


def is_reverse_polarity(a, b):
    return a.lower() == b.lower() and a != b


def remove_once(data):
    set_chars = set(list(data.lower()))

    for char in set_chars:
        data = data.replace('{}{}'.format(char, char.upper()), '')
        data = data.replace('{}{}'.format(char.upper(), char), '')

    return data


# This is my first implementation, it's in O(n^2)
def part1_naive(data):

    len_before = len(data)
    len_after = 0

    while len_before != len_after:
        len_before = len(data)
        data = remove_once(data)
        len_after = len(data)

    return data


# This is Fred's algorithm, it's way faster! O(n)
def part1(data):

    index = 0
    while index < len(data) - 1:
        if (
            data[index].lower() == data[index + 1].lower()
            and data[index] != data[index + 1]
        ):
            data = data[:index] + data[index + 2 :]
            index -= 2
            if index < 0:
                index = -1

        index += 1

    return data


def part2(data):
    data = part1(data)  # We can use the already reduced version
    # to avoid unnecessary computations

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
