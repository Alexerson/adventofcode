def part1(data, limit) -> int:
    spoken = {}
    last_number = 0

    for turn, value in enumerate(data):
        spoken[value] = [turn + 1]
        last_number = value

    for turn in range(len(data) + 1, limit + 1):
        if last_number not in spoken:
            last_number = 0
        else:
            if len(spoken[last_number]) == 1:
                last_number = 0
            else:
                last_number = spoken[last_number][-1] - spoken[last_number][-2]
        if last_number not in spoken:
            spoken[last_number] = []

        spoken[last_number].append(turn)

    return last_number


if __name__ == '__main__':
    mydata = [0, 3, 6]
    # mydata = [1, 2, 16, 19, 18, 0]

    print('Data is: ', mydata)

    print('Solution of 1 is', part1(mydata, 2020))
    print('Solution of 2 is', part1(mydata, 30000000))
