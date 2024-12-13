from src.utils import assert_result, data_import


def perimeter(
    garden: set[tuple[int, int]],
) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    """Returns the list of oriented edges of the garden"""
    edges: set[tuple[tuple[int, int], tuple[int, int]]] = set()

    for cell in garden:
        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_cell = (cell[0] + i, cell[1] + j)
            if new_cell not in garden:
                edges.add((cell, (i, j)))

    return edges


def area(garden: set[tuple[int, int]]) -> int:
    return len(garden)


def build_gardens(data: list[str]) -> dict[int, set[tuple[int, int]]]:
    gardens: dict[int, set[tuple[int, int]]] = {}

    to_explore: dict[tuple[int, int], str] = {}
    for line_no, line in enumerate(data):
        for column_no, cell in enumerate(line):
            to_explore[column_no, line_no] = cell

    current_garden_id = 0
    while to_explore:
        current_cell, current_garden_value = to_explore.popitem()
        current_garden_items = {current_cell}
        current_garden = {current_cell}

        while current_garden_items:
            line_no, column_no = current_garden_items.pop()
            candidates = [
                (line_no - 1, column_no),
                (line_no + 1, column_no),
                (line_no, column_no - 1),
                (line_no, column_no + 1),
            ]

            for candidate in candidates:
                if to_explore.get(candidate) == current_garden_value:
                    current_garden_items.add(candidate)
                    current_garden.add(candidate)

                    del to_explore[candidate]

        gardens[current_garden_id] = current_garden
        current_garden_id += 1

    return gardens


def part1(data: list[str]) -> int:
    gardens = build_gardens(data)
    return sum(
        len(perimeter(garden)) * area(garden) for garden in gardens.values()
    )


def print_garden(
    garden: set[tuple[int, int]],
    current: tuple[int, int] | None = None,
    orientation: tuple[int, int] | None = None,
) -> None:
    if not garden:
        return
    min_x = min(i[0] for i in garden)
    max_x = max(i[0] for i in garden)
    min_y = min(i[1] for i in garden)
    max_y = max(i[1] for i in garden)

    orientation_string = {
        (0, 1): 'v',
        (1, 0): '>',
        (0, -1): '^',
        (-1, 0): '<',
        None: '.',
    }[orientation]

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == current:
                print(orientation_string, end='')
            elif (x, y) in garden:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def sides(garden: set[tuple[int, int]]) -> int:
    edges = perimeter(garden)

    # We only want to count the start of each edge
    return sum(
        (
            (current[0] + orientation[1], current[1] - orientation[0]),
            orientation,
        )
        not in edges
        for current, orientation in edges
    )


def tests() -> None:
    assert len(perimeter({(0, 0)})) == 4
    assert len(perimeter({(0, 0), (0, 1)})) == 6
    assert len(perimeter({(0, 0), (0, 1), (1, 0), (1, 1)})) == 8
    assert len(perimeter({(0, 0), (0, 1), (1, 1)})) == 8
    assert len(perimeter({(0, 0), (1, 0), (1, 1), (2, 1)})) == 10

    # A
    assert sides({(0, 0)}) == 4

    # AA
    assert sides({(0, 0), (0, 1)}) == 4

    # AA
    # AA
    assert sides({(0, 0), (0, 1), (1, 0), (1, 1)}) == 4

    # AA
    #  A
    assert sides({(0, 0), (1, 0), (1, 1)}) == 6

    # AA
    #  AA
    assert sides({(0, 0), (1, 0), (1, 1), (2, 1)}) == 8

    # AAA
    # A
    # AAA
    # A
    # AAA
    assert (
        sides({
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (0, 3),
            (0, 4),
            (1, 4),
            (2, 4),
        })
        == 12
    )

    # AAAAAA
    # AAA  A
    # AAA  A
    # A  AAA
    # A  AAA
    # AAAAAA
    assert (
        sides({
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (5, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (5, 2),
            (0, 3),
            (3, 3),
            (4, 3),
            (5, 3),
            (0, 4),
            (3, 4),
            (4, 4),
            (5, 4),
            (0, 5),
            (1, 5),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 5),
        })
        == 12
    )


def part2(data: list[str]) -> int:
    gardens = build_gardens(data)
    return sum(sides(garden) * area(garden) for garden in gardens.values())


if __name__ == '__main__':
    tests()

    example = data_import('data/y2024/day12-example')
    mydata = data_import('data/y2024/day12')

    assert_result(part1(example), 140)
    print('Solution of 1 is', part1(mydata))  # 27 min 03

    assert_result(part2(example), 80)
    print('Solution of 2 is', part2(mydata))  # Paused at 32:47  x min y
