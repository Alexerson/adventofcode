def get_power(x, y, serial):
    rack_id = x + 10
    power = (rack_id * y + serial) * rack_id
    power = power // 100 % 10

    return power - 5


def part1(serial, size=3, grid=None):
    coordinates = (0, 0)
    max_level = 0

    if grid is None:
        grid = {
            (i, j): get_power(i, j, serial)
            for i in range(1, 301)
            for j in range(1, 3011)
        }

    powers = {}

    for x in range(1, 302 - size):
        for y in range(1, 302 - size):
            if (x - 1, y) in powers:
                power = (
                    powers[x - 1, y]
                    - sum(grid[x - 1, y + j] for j in range(size))
                    + sum(grid[x + size - 1, y + j] for j in range(size))
                )

            elif (x, y - 1) in powers:
                power = (
                    powers[x, y - 1]
                    - sum(grid[x + i, y - 1] for i in range(size))
                    + sum(grid[x + i, y + size - 1] for i in range(size))
                )

            else:
                power = sum(
                    grid[x + i, y + j]
                    for i in range(size)
                    for j in range(size)
                )

            powers[x, y] = power
            if power > max_level:
                max_level = power
                coordinates = (x, y)

    return coordinates, max_level


def part2(serial, max_size=300):
    coordinates = (0, 0, 0)
    max_level = 0
    max_size_i = 0

    grid = {
        (i, j): get_power(i, j, serial)
        for i in range(1, 301)
        for j in range(1, 3011)
    }

    for size in range(1, max_size + 1):
        coord, level = part1(serial, size, grid)
        if level > max_level:
            max_level = level
            coordinates = coord
            max_size_i = size
            print('So far: ', coordinates, max_size_i, max_level)

    return coordinates, max_size_i, max_level


if __name__ == '__main__':
    print('Solution of 1 is', part1(1308))
    print('Solution of 2 is (this will take a lof of time to generate)')
    print(part2(1308))
