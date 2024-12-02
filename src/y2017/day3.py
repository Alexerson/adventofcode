from utils import data_import


def part1(data):
    current = [0, 0]
    direction = 'right'

    max_x = 0
    max_y = 0

    for _i in range(1, data + 1):
        last = tuple(current)

        if direction == 'right':
            current[0] += 1
            if current[0] > max_x:
                direction = 'up'
                max_x = current[0]

        elif direction == 'up':
            current[1] += 1
            if current[1] > max_y:
                max_y = current[1]
                direction = 'left'

        elif direction == 'left':
            current[0] -= 1
            if -current[0] >= max_x:
                direction = 'down'

        elif direction == 'down':
            current[1] -= 1
            if -current[1] >= max_y:
                direction = 'right'

    return sum(abs(i) for i in last)


def part2(data):
    position = {(0, 0): 1}

    current = [0, 0]
    direction = 'right'

    max_x = 0
    max_y = 0

    loop = 0

    while loop < 100:
        loop += 1
        last = tuple(current)

        total = sum(
            position.get((current[0] + i, current[1] + j), 0)
            for i in range(-1, 2)
            for j in range(-1, 2)
        )

        position[last] = total

        if position[last] > data:
            return position[last]

        if direction == 'right':
            current[0] += 1
            if current[0] > max_x:
                direction = 'up'
                max_x = current[0]

        elif direction == 'up':
            current[1] += 1
            if current[1] > max_y:
                max_y = current[1]
                direction = 'left'

        elif direction == 'left':
            current[0] -= 1
            if -current[0] >= max_x:
                direction = 'down'

        elif direction == 'down':
            current[1] -= 1
            if -current[1] >= max_y:
                direction = 'right'

    return None


if __name__ == '__main__':
    data = data_import('data/y2017/day3', int)[0]
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
