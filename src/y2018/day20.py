from src.utils import data_import


def build_tree(regexp):
    doors = {}
    current_positions = {(0, 0)}
    stack = []  # a stack keeping track of (starts, ends) for groups
    starts, ends = (
        {(0, 0)},
        set(),
    )  # current possible starting and ending positions

    directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

    for c in regexp:
        if c == '|':
            # an alternate: update possible ending points,
            # and restart the group
            ends.update(current_positions)
            current_positions = starts
        elif c in 'NESW':
            # move in a given direction:
            # add all edges and update our current positions
            direction = directions[c]
            next_positions = set()
            for position in current_positions:
                next_position = (
                    position[0] + direction[0],
                    position[1] + direction[1],
                )
                if position not in doors:
                    doors[position] = set()
                next_positions.add(next_position)
                doors[position].add(next_position)
            current_positions = next_positions
        elif c == '(':
            # start of group: add current positions as start of a new group
            stack.append((starts, ends))
            starts, ends = current_positions, set()
        elif c == ')':
            # end of group: finish current group,
            # add current positions as possible ends
            current_positions.update(ends)
            starts, ends = stack.pop()

    return doors


def get_distances(doors):
    distances = {}

    todo = {((0, 0), 0)}

    while todo:
        position, distance = todo.pop()

        if position not in distances or distance < distances[position]:
            distances[position] = distance
            todo.update(
                (new_position, distance + 1)
                for new_position in doors.get(position, [])
            )

    return distances


def part1(data):
    doors = build_tree(data[1:-1])

    distances = get_distances(doors)

    return max(distances.values())


def part2(data):
    doors = build_tree(data[1:-1])

    distances = get_distances(doors)

    return sum(distance >= 1000 for distance in distances.values())


if __name__ == '__main__':
    data_example = data_import('data/day20_example', str)[0]
    data_real = data_import('data/day20_real', str)[0]
    print('Solution of 1 is', part1(data_example))
    print('Solution of 1 is', part1(data_real))
    print('Solution of 2 is', part2(data_real))
