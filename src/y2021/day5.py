from typing import NamedTuple

from utils import data_import


class Line(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int

    def crossed(
        self, consider_only_horizontal_or_vertical: bool = False
    ) -> list[tuple[int, int]]:
        if self.x1 == self.x2:
            x = self.x1
            y_min = min(self.y1, self.y2)
            y_max = max(self.y1, self.y2)
            return [(x, y) for y in range(y_min, y_max + 1)]

        if self.y1 == self.y2:
            x_min = min(self.x1, self.x2)
            x_max = max(self.x1, self.x2)
            y = self.y1
            return [(x, y) for x in range(x_min, x_max + 1)]

        if consider_only_horizontal_or_vertical:
            return []

        step = (self.y2 - self.y1) / (self.x2 - self.x1)

        out = []
        x_min = min(self.x1, self.x2)
        x_max = max(self.x1, self.x2)
        for i in range(x_min, x_max + 1):
            y = int(self.y1 + (i - self.x1) * step)
            out.append((i, y))

        return out


def convert(data: list[str]) -> list[Line]:
    out = []
    for item in data:
        p1, p2 = item.split('->')
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        out.append(Line(int(x1), int(y1), int(x2), int(y2)))

    return out


def part1(data: list[Line]) -> int:
    crossed = {}
    for line in data:
        for x in line.crossed(consider_only_horizontal_or_vertical=True):
            if x not in crossed:
                crossed[x] = 0
            crossed[x] += 1

    return sum(1 for x in crossed.values() if x > 1)


def part2(data: list[Line]) -> int:
    crossed = {}
    for line in data:
        for p in line.crossed(consider_only_horizontal_or_vertical=False):
            if p not in crossed:
                crossed[p] = 0
            crossed[p] += 1

    return sum(1 for x in crossed.values() if x > 1)


if __name__ == '__main__':
    # mydata = data_import('data/y2021/day5_example')
    mydata = data_import('data/y2021/day5')

    mydata = convert(mydata)
    print('Input is', mydata)
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
