def part1(depth, target):
    cave = {}

    total = 0

    for i in range(0, target[0] + 1):
        for j in range(0, target[1] + 1):

            if i == 0:
                cave[i, j] = {'index': 48271 * j}

            elif j == 0:
                cave[i, j] = {'index': 16807 * i}

            else:
                cave[i, j] = {
                    'index': cave[i - 1, j]['level'] * cave[i, j - 1]['level']
                }

            cave[i, j]['level'] = (cave[i, j]['index'] + depth) % 20183
            cave[i, j]['erosion'] = cave[i, j]['level'] % 3

            total += cave[i, j]['erosion']

    total -= cave[target]['erosion']
    cave[target] = {'index': 0, 'level': depth % 20183, 'erosion': 0}

    return cave, total


elts = {0: '.', 1: '=', 2: '|'}


def show_cave(cave, target):
    for j in range(0, target[0] + 1):
        line = ''
        for i in range(0, target[1] + 1):
            line += elts[cave[i, j]['erosion']]
        print(line)


def part2(data):
    pass


if __name__ == '__main__':
    depth = 11109
    target = 9, 731

    print('Solution of 1 is', part1(depth, target)[1])
    print('Solution of 2 is', part2(data))
