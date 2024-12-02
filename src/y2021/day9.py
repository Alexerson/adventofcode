import contextlib
import math

from src.utils import data_import


def convert_data(data: list[str]) -> list[list[int]]:
    return [[int(x) for x in line] for line in data]


def part1(data: list[list[int]]) -> int:
    low_points = []

    for x, line in enumerate(data):
        for y, item in enumerate(line):
            neighbours = []
            with contextlib.suppress(IndexError):
                neighbours.append(data[x - 1][y])

            with contextlib.suppress(IndexError):
                neighbours.append(data[x + 1][y])

            with contextlib.suppress(IndexError):
                neighbours.append(line[y - 1])

            with contextlib.suppress(IndexError):
                neighbours.append(line[y + 1])

            if all(item < neighbour for neighbour in neighbours):
                low_points.append((item + 1, x, y))

    return sum(x[0] for x in low_points)


def part2(data: list[list[int]]) -> int:
    bassins: dict[tuple[int, int], int] = {}
    bassin_id = 0
    bassin_reverse: dict[int, list[tuple[int, int]]] = {}

    for level in range(9):
        for x, line in enumerate(data):
            for y, item in enumerate(line):
                if item != level:
                    continue
                neighbours = set()
                with contextlib.suppress(KeyError):
                    neighbours.add(bassins[x - 1, y])

                with contextlib.suppress(KeyError):
                    neighbours.add(bassins[x + 1, y])

                with contextlib.suppress(KeyError):
                    neighbours.add(bassins[x, y - 1])

                with contextlib.suppress(KeyError):
                    neighbours.add(bassins[x, y + 1])

                # We have a new bassin
                if len(neighbours) == 0:
                    bassins[x, y] = bassin_id
                    bassin_id += 1

                # We are in the same bassin as all the neighbours
                elif len(neighbours) == 1:
                    bassins[x, y] = neighbours.pop()

                # There are multiple bassins, merge them
                else:
                    common_bassin = neighbours.pop()
                    for other_bassin in neighbours:
                        for i, j in bassin_reverse[other_bassin]:
                            bassins[i, j] = common_bassin
                        bassin_reverse[common_bassin] += bassin_reverse[
                            other_bassin
                        ]

                        bassins[x, y] = common_bassin

                # Keep track of the reverse bassin
                if bassins[x, y] not in bassin_reverse:
                    bassin_reverse[bassins[x, y]] = []
                bassin_reverse[bassins[x, y]].append((x, y))

    return math.prod(
        sorted(
            (len(bassin) for bassin in bassin_reverse.values()), reverse=True
        )[:3],
    )


if __name__ == '__main__':
    # mydata = data_import('data/y2021/day9_example')
    mydata = data_import('data/y2021/day9')

    mydata = convert_data(mydata)

    print('Input is', mydata)

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
