from utils import data_import


def part1(data: list[str]) -> int:
    counts0 = [0] * len(data[0])
    counts1 = [0] * len(data[0])

    for line in data:
        for index, char in enumerate(line):
            if char == '0':
                counts0[index] += 1
            if char == '1':
                counts1[index] += 1

    gamma = ''
    epsilon = ''

    for c0, c1 in zip(counts0, counts1):
        if c0 > c1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)


def rating(data: list[str], majority=True) -> str:
    bits = len(data[0])

    candidates = data

    for bit in range(bits):
        zeros = [item for item in candidates if item[bit] == '0']
        ones = [item for item in candidates if item[bit] == '1']

        if majority:
            candidates = zeros if len(zeros) > len(ones) else ones
        elif len(zeros) <= len(ones):
            candidates = zeros
        else:
            candidates = ones

        if len(candidates) == 1:
            return candidates[0]

    return candidates[0]


def part2(data: list[str]) -> int:
    return int(rating(data, True), 2) * int(rating(data, False), 2)


if __name__ == '__main__':
    # mydata = data_import('data/y2021/day3_example')
    mydata = data_import('data/y2021/day3')
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
