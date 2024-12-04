from src.utils import data_import


def total_horizontal_words(data: list[str], lookup: str) -> int:
    search = {lookup, lookup[::-1]}
    total = 0
    for line in data:
        word = line[:4]
        if word in search:
            total += 1
        for cell in line[4:]:
            word = word[1:] + cell
            if word in search:
                total += 1

    return total


def transpose(data: list[str]) -> list[str]:
    return [''.join(col) for col in zip(*data)]  # type: ignore[misc]


def make_diagonal(data: list[str], to_the_right: bool = True) -> list[str]:
    data_diagonal = []
    for index, line in enumerate(data):
        if to_the_right:
            data_diagonal.append(
                'O' * index + line + 'O' * (len(data) - index)
            )
        else:
            data_diagonal.append(
                (len(data) - index) * 'O' + line + index * 'O'
            )
    return data_diagonal


def part1(data: list[str]) -> int:
    total = 0

    total += total_horizontal_words(data, 'XMAS')
    total += total_horizontal_words(transpose(data), 'XMAS')
    total += total_horizontal_words(transpose(make_diagonal(data)), 'XMAS')
    total += total_horizontal_words(
        transpose(make_diagonal(data, False)), 'XMAS'
    )

    return total


def part2(data: list[str]) -> int:
    width = len(data[0])
    height = len(data)
    total = 0

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            center = data[i][j]
            if center != 'A':
                continue

            top_left = data[i - 1][j - 1]
            top_right = data[i - 1][j + 1]
            bottom_left = data[i + 1][j - 1]
            bottom_right = data[i + 1][j + 1]

            word1 = top_left + center + bottom_right
            word2 = top_right + center + bottom_left

            if (word1 != 'MAS' and word1 != 'SAM') or (
                word2 != 'MAS' and word2 != 'SAM'
            ):
                continue
            total += 1

    return total


if __name__ == '__main__':
    example_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip().split('\n')

    assert part1(example_data) == 18
    assert part2(example_data) == 9

    mydata = data_import('data/y2024/day4')
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
