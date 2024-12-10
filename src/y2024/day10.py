from src.utils import assert_result, data_import


def next_steps(
    altitudes: dict[tuple[int, int], int],
    position: tuple[int, int],
    current_height: int,
) -> set[tuple[int, int]]:
    x, y = position

    candidates = {(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)}

    return {
        candidate
        for candidate in candidates
        if altitudes.get(candidate) == current_height + 1
    }


def score_trailhead_1(
    altitudes: dict[tuple[int, int], int], trailhead: tuple[int, int]
) -> int:
    current_positions = {trailhead}
    for altitude in range(9):
        new_positions = set()
        for position in current_positions:
            new_positions |= next_steps(altitudes, position, altitude)

        current_positions = new_positions

    return len(current_positions)


def score_trailhead_2(
    altitudes: dict[tuple[int, int], int], trailhead: tuple[int, int]
) -> int:
    current_positions: dict[tuple[int, int], int] = {trailhead: 1}

    for altitude in range(9):
        new_positions: dict[tuple[int, int], int] = {}
        for position, paths in current_positions.items():
            next_positions = next_steps(altitudes, position, altitude)
            for new_position in next_positions:
                new_positions[new_position] = (
                    new_positions.get(new_position, 0) + paths
                )

        current_positions = new_positions

    return sum(current_positions.values())


def part1(altitudes: dict[tuple[int, int], int]) -> int:
    trailheads = {
        position for position, height in altitudes.items() if height == 0
    }

    return sum(
        score_trailhead_1(altitudes, trailhead) for trailhead in trailheads
    )


def part2(altitudes: dict[tuple[int, int], int]) -> int:
    trailheads = {
        position for position, height in altitudes.items() if height == 0
    }

    return sum(
        score_trailhead_2(altitudes, trailhead) for trailhead in trailheads
    )


def convert_to_dict(data: list[str]) -> dict[tuple[int, int], int]:
    return {
        (column_no, row_no): int(cell)
        for row_no, row in enumerate(data)
        for column_no, cell in enumerate(row)
    }


if __name__ == '__main__':
    mydata = data_import('data/y2024/day10-example')

    altitudes = convert_to_dict(mydata)
    assert_result(part1(altitudes), 36)
    assert_result(part2(altitudes), 81)

    mydata = data_import('data/y2024/day10')
    altitudes = convert_to_dict(mydata)
    print('Solution of 1 is', part1(altitudes))  # 16 min 48
    print('Solution of 2 is', part2(altitudes))  # 25 min 27
