def part1(data, limit) -> int:
    spoken = {}
    last_number = 0

    for turn, value in enumerate(data):
        spoken[value] = (None, turn + 1)
        last_number = value

    turn = len(data) + 1

    while turn <= limit:
        try:
            last_number = spoken[last_number][1] - spoken[last_number][0]
        except (TypeError, KeyError):
            last_number = 0

        if last_number in spoken:
            spoken[last_number] = (spoken[last_number][1], turn)
        else:
            spoken[last_number] = (None, turn)
        turn += 1

    return last_number


if __name__ == '__main__':
    # mydata = [0, 3, 6]
    mydata = [1, 2, 16, 19, 18, 0]

    print('Data is: ', mydata)

    print('Solution of 1 is', part1(mydata, 2020))
    print('Solution of 2 is', part1(mydata, 30000000))
