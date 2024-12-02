from time import sleep

from src.utils import data_import

from .intcode import Program


def display_image(image):
    image = image.copy()

    out = ['\nimage:']

    xs = [x for x, y in image]
    ys = [y for x, y in image]

    out.append(
        '\n'.join(
            ''.join(image[x, y] for x in range(min(xs), max(xs) + 1))
            for y in range(min(ys), max(ys) + 1)
        ),
    )
    print('\n'.join(out))
    sleep(0.05)


def explore_space(data):
    program = Program(data)

    stream = []

    while not program.finished:
        output = program.run_until_output()
        if output is not None:
            stream.append(chr(output))

    return stream


def convert_stream_into_image(stream):
    image = {}
    position = [0, 0]

    for pixel in stream:
        if pixel == '\n':
            position[0] = 0
            position[1] += 1
        else:
            image[tuple(position)] = pixel
            position[0] += 1

    return image


def part1(data, debug=False):
    stream = explore_space(data)
    image = convert_stream_into_image(stream)

    xs = [x for x, y in image]
    ys = [y for x, y in image]

    cols = max(xs)
    rows = max(ys)

    if debug:
        intersections = []
    cumsum = 0
    for i in range(cols):
        for j in range(rows):
            if (
                image.get((i - 1, j)) == '#'
                and image.get((i, j - 1)) == '#'
                and image.get((i + 1, j)) == '#'
                and image.get((i, j + 1)) == '#'
            ):
                cumsum += i * j
                if debug:
                    intersections.append((i, j))

    if debug:
        for intersection in intersections:
            image[intersection] = 'O'

        display_image(image)

    return cumsum


def find_next_move(image, position, direction):
    # test left:
    if direction == '^':
        left = (position[0] - 1, position[1])
        right = (position[0] + 1, position[1])
    elif direction == '>':
        left = (position[0], position[1] - 1)
        right = (position[0], position[1] + 1)
    elif direction == 'v':
        left = (position[0] + 1, position[1])
        right = (position[0] - 1, position[1])
    elif direction == '<':
        left = (position[0], position[1] + 1)
        right = (position[0], position[1] - 1)

    if image.get(left) == '#':
        turn = 'L'
        incr = (left[0] - position[0], left[1] - position[1])
    elif image.get(right) == '#':
        turn = 'R'
        incr = (right[0] - position[0], right[1] - position[1])
    else:
        msg = 'EOL'
        raise ValueError(msg)

    times = 1
    current = position[0] + incr[0], position[1] + incr[1]

    while image.get(current) == '#':
        times += 1
        current = current[0] + incr[0], current[1] + incr[1]

    return (turn, times - 1)


def part2(data, debug=False):
    stream = explore_space(data)
    image = convert_stream_into_image(stream)

    position = next(
        (x, y)
        for (x, y), pixel in image.items()
        if pixel in {'^', '>', '<', 'v'}
    )
    direction = image[position]

    moves = []

    while True:
        try:
            turn, duration = find_next_move(image, position, direction)
        except ValueError:
            break

        if direction == '^':
            if turn == 'L':
                direction = '<'
                position = (position[0] - duration, position[1])
            else:
                direction = '>'
                position = (position[0] + duration, position[1])
        elif direction == '>':
            if turn == 'L':
                direction = '^'
                position = (position[0], position[1] - duration)
            else:
                direction = 'v'
                position = (position[0], position[1] + duration)
        elif direction == '<':
            if turn == 'L':
                direction = 'v'
                position = (position[0], position[1] + duration)
            else:
                direction = '^'
                position = (position[0], position[1] - duration)
        elif direction == 'v':
            if turn == 'L':
                direction = '>'
                position = (position[0] + duration, position[1])
            else:
                direction = '<'
                position = (position[0] - duration, position[1])

        moves.extend((turn, duration))

    # moves =
    # A A C B C B C B C A

    # A = R 10 L 12 R 6
    # B = R 10 L 12 L 12
    # C = R 6 R 10 R 12 R 6

    main_routine = 'A,A,C,B,C,B,C,B,C,A'
    function_a = 'R,10,L,12,R,6'
    function_b = 'R,10,L,12,L,12'
    function_c = 'R,6,R,10,R,12,R,6'

    data = data[:]
    data[0] = 2
    program = Program(data)

    inputs = [
        ord(a)
        for a in f'{main_routine}\n{function_a}\n{function_b}\n{function_c}\nn'
        + '\n'
    ]
    outputs = []

    while not program.finished:
        outputs.append(program.run_until_output(inputs))

    outputs = outputs[:-1]
    final_score = outputs[-1]

    if debug:
        print(''.join(chr(a) for a in outputs[:-1]))

    return final_score


if __name__ == '__main__':
    data = data_import('data/y2019/day17', cast=int, split_char=',')[0]
    print('Solution of 1 is', part1(data, debug=False))
    print('Solution of 2 is', part2(data))
