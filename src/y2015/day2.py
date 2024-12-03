from src.utils import data_import


def part1(mydata: list[list[int]]) -> int:
    total = 0
    for length, width, height in mydata:
        sides = [length * width, width * height, height * length]
        smallest_side = min(sides)
        total += 2 * sum(sides) + smallest_side
    return total


def part2(mydata: list[list[int]]) -> int:
    return sum(
        (
            2 * min(length + width, width + height, height + length)
            + length * width * height
        )
        for length, width, height in mydata
    )


if __name__ == '__main__':
    mydata = data_import('data/y2015/day2', cast=int, split_char='x')

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
