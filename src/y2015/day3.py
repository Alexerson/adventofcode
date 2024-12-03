from src.utils import data_import


def part1(mydata: str) -> int:
    visited: set[tuple[int, int]] = set()
    x, y = 0, 0

    for move in mydata:
        match move:
            case '^':
                y += 1
            case 'v':
                y -= 1
            case '>':
                x += 1
            case '<':
                x -= 1
        visited.add((x, y))
    return len(visited)


def part2(mydata: str) -> int:
    visited: set[tuple[int, int]] = set()
    x, y = 0, 0

    for move in mydata[::2]:
        match move:
            case '^':
                y += 1
            case 'v':
                y -= 1
            case '>':
                x += 1
            case '<':
                x -= 1
        visited.add((x, y))

    x, y = 0, 0
    for move in mydata[1::2]:
        match move:
            case '^':
                y += 1
            case 'v':
                y -= 1
            case '>':
                x += 1
            case '<':
                x -= 1
        visited.add((x, y))
    return len(visited)


if __name__ == '__main__':
    mydata = data_import('data/y2015/day3')[0]

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
