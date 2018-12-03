import collections

from utils import data_import


# We need to convert the input in something we can work with
def convert_data(data):
    out = []
    for item in data:
        pk, _, position, size = item.split(" ")
        pk = pk[1:]
        x, y = position[:-1].split(',')
        w, h = size.split('x')
        out.append((pk, int(x), int(y), int(w), int(h)))
    return out


# We need an easy way to iterate over all tuples of a claim
def claim_pairs(x, y, w, h):
    for i in range(x, x + w):
        for j in range(y, y + h):
            yield (i, j)


# This will give a list of all used squares with counts
def squares_usage_count(data):
    return collections.Counter(
        (i, j) for id, x, y, w, h in data for i, j in claim_pairs(x, y, w, h)
    )


# From a list of used squares,
# we simple need to count how many are used more than once
def part1(data):
    return sum(1 for count in squares_usage_count(data).values() if count > 1)


# From a list of used squares,
# We look which claim is using only squares used once
def part2(data):
    overlap_items = squares_usage_count(data)

    for id, x, y, w, h in data:
        if all(overlap_items[(i, j)] == 1 for i, j in claim_pairs(x, y, w, h)):
            return id


if __name__ == '__main__':
    data = data_import('data/day3')
    processed_data = convert_data(data)
    print('Input is', processed_data)
    print('Solution of 1 is', part1(processed_data))
    print('Solution of 2 is', part2(data))
