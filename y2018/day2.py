import collections

import editdistance

from utils import data_import


def part1(data):
    count2 = 0
    count3 = 0
    for item in data:
        counter = collections.Counter(list(item))
        counter = {b: a for a, b in counter.items()}
        if counter.get(2):
            count2 += 1

        if counter.get(3):
            count3 += 1

    return count2, count3, count2 * count3


def part2(data):
    # I was lazy here, I used an existing library to compute difference
    # between ID

    for word1 in data:
        for word2 in data:
            if editdistance.eval(word1, word2) == 1:
                combination = ''.join(
                    letter1
                    for letter1, letter2 in zip(word1, word2)
                    if letter1 == letter2
                )
                return (word1, word2, combination)


if __name__ == '__main__':
    data = data_import('data/day2')
    print('Input is', data)
    print('Solution of 1 is {2} ({0} x {1})'.format(*part1(data)))
    print(
        'Solution of 2 is {2} (Almost equal IDs are {0} & {1})'.format(
            *part2(data)
        )
    )
