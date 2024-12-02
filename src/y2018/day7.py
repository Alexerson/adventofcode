import collections

from src.utils import data_import


def part1(data):
    a, b = list(zip(*data))
    all_chars = sorted(set(a + b))

    out = []

    while data:
        counter = collections.Counter(list(zip(*data))[1])

        for char in all_chars:
            if not counter.get(char) and char not in out:
                out.append(char)
                break

        data = [item for item in data if item[0] not in out]

    for a in sorted(all_chars):
        if a not in out:
            out.append(a)

    return ''.join(out)


def part2(data, workers=5, duration=60):
    a, b = list(zip(*data))
    all_chars = sorted(set(a + b))

    durations = {
        char: index + 1 + duration for index, char in enumerate(all_chars)
    }

    time = 0
    ends_work = {}

    out = []

    len_all_chars = len(all_chars)

    while len(out) < len_all_chars:
        counter = collections.Counter(list(zip(*data))[1]) if data else {}

        for char in all_chars:
            if (not counter.get(char) and char not in out) and (
                char not in ends_work and len(ends_work.keys()) < workers
            ):
                ends_work[char] = time + durations[char]

        time += 1

        for char in all_chars:
            if char in ends_work and ends_work.get(char) <= time:
                out.append(char)
                del ends_work[char]

        data = [item for item in data if item[0] not in out]

    return time


if __name__ == '__main__':
    data = data_import('data/day7')
    data = [(item[5], item[-12]) for item in data if item.strip()]

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
