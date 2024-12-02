import itertools

from utils import data_import


def apply_mask_v1(mask, value):
    ones = mask.replace('X', '0')
    zeros = mask.replace('X', '1')

    return (int(ones, 2) | value) & int(zeros, 2)


def apply_mask_v2(mask, value):
    binary = format(value, 'b').rjust(36, '0')

    result = ''.join(
        (mask_char == '1' and '1') or (mask_char == 'X' and 'X') or char
        for char, mask_char in zip(binary, mask)
    )

    out = []

    xs_indexes = [index for index, char in enumerate(result) if char == 'X']

    for values in itertools.product(['0', '1'], repeat=len(xs_indexes)):
        result_base = list(result)
        for value, index in zip(values, xs_indexes):
            result_base[index] = value
        out.append(int(''.join(result_base), 2))
    return out


def part1(data) -> int:
    mask = ''
    mem = {}

    for key, value in data:
        if key == 'mask':
            mask = value

        else:
            index = int(key[4:-1])
            mem[index] = apply_mask_v1(mask, int(value))

    return sum(mem.values())


def part2(data) -> int:
    mask = ''
    mem = {}

    for key, value in data:
        if key == 'mask':
            mask = value

        else:
            index = int(key[4:-1])

            for address in apply_mask_v2(mask, index):
                mem[address] = int(value)

    return sum(mem.values())


if __name__ == '__main__':
    mydata = data_import('data/y2020/day14', split_char=' = ')

    print('Data is: ', mydata[:10])

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
