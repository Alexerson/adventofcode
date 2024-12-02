from utils import data_import


def is_valid(passphrase, anagram=False):
    known = set()

    for word in passphrase.split():
        if anagram:
            word = ''.join(sorted(word))
        if word in known:
            return False
        known.add(word)
    return True


def part1(data):
    return sum(is_valid(passphrase) for passphrase in data)


def part2(data):
    return sum(is_valid(passphrase, True) for passphrase in data)


if __name__ == '__main__':
    data = data_import('data/y2017/day4')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
