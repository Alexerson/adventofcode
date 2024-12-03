import collections
import itertools

from src.utils import data_import


def part1(mydata: list[str]) -> int:
    def is_nice(s: str) -> bool:
        all_letters = set(s)

        counts = collections.Counter(s)
        if (
            counts['a'] + counts['e'] + counts['i'] + counts['o'] + counts['u']
            < 3
        ):
            return False

        have_duplicate = False
        for letter in all_letters:
            have_duplicate = letter * 2 in s
            if have_duplicate:
                break

        if not have_duplicate:
            return False

        return all(naughty not in s for naughty in ['ab', 'cd', 'pq', 'xy'])

    assert is_nice('ugknbfddgicrmopn')
    assert is_nice('aaaa')
    assert not is_nice('jchzalrnumimnmhp')
    assert not is_nice('haegwjzuvuyypxyu')
    assert not is_nice('dvszwmarrgswjxmb')

    return sum(is_nice(s) for s in mydata)


def part2(mydata: list[str]) -> int:
    def is_nice(s: str) -> bool:
        def has_two_pairs(s: str) -> bool:
            letters = set(s)
            for pair in itertools.combinations_with_replacement(letters, 2):
                if len(s.split(''.join(pair))) >= 3:
                    return True
                if len(s.split(''.join(pair[::-1]))) >= 3:
                    return True
            return False

        def has_trigram(s: str) -> bool:
            letters = set(s)
            for l0, l1 in itertools.combinations_with_replacement(letters, 2):
                if f'{l0}{l1}{l0}' in s:
                    return True
                if f'{l1}{l0}{l1}' in s:
                    return True
            return False

        return has_two_pairs(s) and has_trigram(s)

    assert is_nice('qjhvhtzxzqqjkmpb')
    assert is_nice('xxyxx')
    assert not is_nice('uurcxstgmygtbstg')
    assert not is_nice('ieodomkazucvgmuy')

    return sum(is_nice(s) for s in mydata)


if __name__ == '__main__':
    mydata = data_import('data/y2015/day5')

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
