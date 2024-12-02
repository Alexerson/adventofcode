from src.utils import data_import


def is_safe(levels: list[int]) -> bool:
    increasing = None

    current = levels[0]
    for next in levels[1:]:
        if increasing is None:
            increasing = next > current

        if increasing != (next > current):
            return False

        if not (1 <= abs(next - current) <= 3):
            return False

        current = next

    return True


def is_safe_tolerant(levels: list[int]) -> bool:
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1 :]):
            return True

    return False


def part1(data: list[list[int]]) -> int:
    return sum(is_safe(d) for d in data)


def part2(data: list[list[int]]) -> int:
    return sum(is_safe_tolerant(d) for d in data)


if __name__ == '__main__':
    mydata = data_import('data/y2024/day2', int, split_char=' ')
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
