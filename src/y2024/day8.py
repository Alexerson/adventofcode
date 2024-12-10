import itertools

from src.utils import assert_result, data_import


def map_to_frequencies_dict(
    data: list[str],
) -> dict[str, set[tuple[int, int]]]:
    frequencies: dict[str, set[tuple[int, int]]] = {}
    for line_no, line in enumerate(data):
        for column_no, cell in enumerate(line):
            if cell == '.':
                continue

            if cell not in frequencies:
                frequencies[cell] = set()

            frequencies[cell].add((column_no, line_no))

    return frequencies


def part1(data: list[str]) -> int:
    width = len(data[0])
    height = len(data)
    antinodes: set[tuple[int, int]] = set()
    for positions in map_to_frequencies_dict(data).values():
        for a, b in itertools.combinations(positions, 2):
            antinodes.add((
                2 * a[0] - b[0],
                2 * a[1] - b[1],
            ))

            antinodes.add((
                2 * b[0] - a[0],
                2 * b[1] - a[1],
            ))

    return sum(
        0 <= position[0] < width and 0 <= position[1] < height
        for position in antinodes
    )


def part2(data: list[str]) -> int:
    width = len(data[0])
    height = len(data)

    antinodes: set[tuple[int, int]] = {
        (
            a[0] + i * (a[0] - b[0]),
            a[1] + i * (a[1] - b[1]),
        )
        for positions in map_to_frequencies_dict(data).values()
        for a, b in itertools.combinations(positions, 2)
        for i in range(-max(width, height), max(width, height))
    }

    return sum(
        0 <= position[0] < width and 0 <= position[1] < height
        for position in antinodes
    )


if __name__ == '__main__':
    mydata = data_import('data/y2024/day8-example')
    assert_result(part1(mydata), 14)
    assert_result(part2(mydata), 34)

    mydata = data_import('data/y2024/day8')
    print('Solution of 1 is', part1(mydata))  # 27 min
    print('Solution of 2 is', part2(mydata))  # 33 min 04
