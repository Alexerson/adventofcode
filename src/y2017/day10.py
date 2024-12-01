from utils import data_import


def part1(data, count=255, rounds=1):
    cord = list(range(count))

    skip_size = 0
    current_position = 0

    for length in data * rounds:
        end_position = current_position + length

        if end_position > count:
            sub_cord = cord[current_position:] + cord[: end_position % count]
        else:
            sub_cord = cord[current_position:end_position]

        sub_cord = list(reversed(sub_cord))
        if end_position > count:
            cord = (
                sub_cord[(count - current_position) :]
                + cord[end_position % count : current_position]
                + sub_cord[: (count - current_position)]
            )
        else:
            cord = cord[:current_position] + sub_cord + cord[end_position:]

        current_position = (current_position + skip_size + length) % count

        skip_size += 1

    return cord


def xor(data):
    result = data[0]

    for item in data[1:]:
        result = result ^ item

    return result


def part2(data, count=256, rounds=64):
    data_ = [ord(b) for b in data] + [17, 31, 73, 47, 23]
    sparse_hash = part1(data_, count, rounds)

    out = ''
    for i in range(16):
        out += hex(xor(sparse_hash[i * 16 : (i + 1) * 16]))[2:]

    return out


if __name__ == '__main__':
    data = data_import('2017/data/day10_example', int, ',')[0]
    print('Example:')
    print('Solution of 1 is', part1(data, 5))
    print('Solution of 2 is', part2(data, 5))

    print('Real:')
    data = data_import('2017/data/day10_real', int, ',')[0]
    data_ints = [int(item) for item in data.split(',')]
    hash = part1(data_ints, 256)
    print('Solution of 1 is', hash[0] * hash[1])
    print('Solution of 2 is', part2(data))
