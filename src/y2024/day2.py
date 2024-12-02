from utils import data_import


def is_safe(levels: list[int]) -> bool:
    # All increasing or decreasing:
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False

    current = levels[0]
    for next in levels[1:]:
        if next == current:
            return False

        if abs(next - current) > 3:
            return False

        current = next

    return True


def part1(data: list[list[int]]) -> int:
    return sum(is_safe(d) for d in data)


def part2(data: list[list[int]]) -> int:
    total_safe = 0

    for levels in data:
        if is_safe(levels):
            total_safe += 1
            print(levels, 'safe')
            continue

        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1 :]):
                print(levels, 'safe if removing', levels[i])
                total_safe += 1
                break

    return total_safe


if __name__ == '__main__':
    mydata = data_import('data/y2024/day2', int, split_char=' ')
    # print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
