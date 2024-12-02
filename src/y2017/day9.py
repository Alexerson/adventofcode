from src.utils import data_import


def part1(data):
    score = 0
    current_score = 0
    is_garbage = False
    ignore_next = False

    garbage_count = 0

    for item in data:
        if ignore_next:
            ignore_next = False
            continue

        if item == '!':
            ignore_next = True
            continue

        if is_garbage:
            if item == '>':
                is_garbage = False
            garbage_count += 1
            continue

        if item == '<':
            is_garbage = True
            garbage_count -= 1
            continue

        if item == '{':
            current_score += 1
            continue

        if item == '}':
            score += current_score
            current_score -= 1
            continue

    return score, garbage_count


if __name__ == '__main__':
    data = data_import('data/day9_example', str)
    data = ''.join(data[0])
    print('Example:')
    print('Solution of 1 is', part1(data)[0])
    print('Solution of 2 is', part1(data)[1])

    print('Real:')
    data = data_import('data/day9_real', str)
    data = ''.join(data[0])
    print('Solution of 1 is', part1(data)[0])
    print('Solution of 2 is', part1(data)[1])
