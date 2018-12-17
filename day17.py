from PIL import Image

from utils import data_import


def convert_data(data):
    clay = {}
    for x, y in data:

        if x[0] == 'x':
            column = int(x[2:])
            y = y[2:]
            line_min, line_max = y.split('..')
            for line in range(int(line_min), int(line_max) + 1):
                clay[(column, line)] = True
        else:
            line = int(x[2:])
            y = y[2:]
            column_min, column_max = y.split('..')
            for column in range(int(column_min), int(column_max) + 1):
                clay[(column, line)] = True

    return clay


def show_state(clay, water, candidates, save=False):
    min_x = min(x for x, y in list(water.keys()) + list(clay.keys()))
    max_x = max(x for x, y in list(water.keys()) + list(clay.keys()))
    max_y = max(y for x, y in list(water.keys()) + list(clay.keys()))

    canvas = Image.new("L", (max_x - min_x + 1, max_y + 1))

    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in candidates:
                canvas.putpixel((x - min_x, y), 180)
            elif clay.get((x, y)):
                canvas.putpixel((x - min_x, y), 255)
            else:
                water_elt = water.get((x, y))
                if water_elt == RUNNING:
                    canvas.putpixel((x - min_x, y), 128)
                elif water_elt == STILL:
                    canvas.putpixel((x - min_x, y), 100)
    if save:
        canvas.save("day17.png")
    else:
        canvas.show()


RUNNING = 1
RUNNING_DONE = 3
STILL = 2


def get_bounds(column, line, clay, water):
    this_line = [(x, y) for x, y in clay.keys() if y == line]

    try:
        left_bound = max(x for x, y in this_line if x < column)
        right_bound = min(x for x, y in this_line if x > column)
    except ValueError:
        return

    for x in range(left_bound, right_bound + 1):
        if not clay.get((x, line + 1)) and not water.get((x, line + 1)):
            return

    return (left_bound + 1, right_bound - 1)


def flow_one(candidate, clay, water, max_y):
    x, y = candidate

    # Fill column
    try:
        bottom_clay = min(y_ for x_, y_ in clay.keys() if x_ == x and y_ > y)
    except ValueError:
        bottom_clay = max_y + 1
    try:
        bottom_water = min(
            y_
            for x_, y_ in water.keys()
            if x_ == x and y_ > y and water.get((x_, y_)) == STILL
        )
    except ValueError:
        bottom_water = max_y + 1
    bottom = min(bottom_clay, bottom_water)
    for y_ in range(y + 1, bottom):
        if (x, y_) not in water:
            water[(x, y_)] = RUNNING

    if bottom != y + 1:
        return [(x, bottom - 1)]

    if bottom == max_y + 1:
        return []

    candidates = []

    # Is the next one clay or still?
    if clay.get((x, y + 1)) or water.get((x, y + 1)) == STILL:
        # Is it bounded by clay or water?
        bounds = get_bounds(x, y, clay, water)
        if bounds:
            for x_ in range(bounds[0], bounds[1] + 1):
                water[(x_, y)] = STILL
                if water.get((x_, y - 1)) == RUNNING:
                    candidates.append((x_, y - 1))

        # Expand to the left:
        if not clay.get((x - 1, y)) and not water.get((x - 1, y)):
            water[(x - 1, y)] = RUNNING
            candidates.append((x - 1, y))
        # Expand to the right:
        if not clay.get((x + 1, y)) and not water.get((x + 1, y)):
            water[(x + 1, y)] = RUNNING
            candidates.append((x + 1, y))
    else:
        # Shouldn't happen because we fill columns whenever possible
        water[(x, y + 1)] = RUNNING
        candidates.append((x, y + 1))

    return candidates


def run_simulation(data):
    clay = convert_data(data)
    water = {}

    min_y = min(y for x, y in clay.keys())
    max_y = max(y for x, y in clay.keys())

    candidates = [(500, min_y - 1)]

    while candidates:
        candidate = candidates.pop()

        new_candidates = flow_one(candidate, clay, water, max_y)

        candidates += new_candidates

    return clay, water


def part1(clay, water):
    return len(water)


def part2(clay, water):
    return sum(w == STILL for w in water.values())


if __name__ == '__main__':
    data_example = data_import('data/day17_example', str, ',')
    clay, water = run_simulation(data_example)
    print('Solution of 1 is', part1(clay, water))
    print('Solution of 2 is', part2(clay, water))

    data_real = data_import('data/day17', str, ',')
    clay, water = run_simulation(data_real)
    print('Solution of 1 is', part1(clay, water))
    print('Solution of 2 is', part2(clay, water))
