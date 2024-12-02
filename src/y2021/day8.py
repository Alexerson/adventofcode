from utils import data_import


def convert(data: list[str]) -> list[tuple[list[str], list[str]]]:
    return [(item[0].split(), item[1].split()) for item in data]


def part1(data: list[tuple[list[str], list[str]]]) -> int:
    outputs = [output for _, output in data]

    return sum(
        len(item) in {2, 3, 4, 7} for signal in outputs for item in signal
    )


def rewire(inputs: list[str]) -> dict[str, int]:
    wires = {}
    wires_reverse = {}
    for input in inputs:
        hash = ''.join(sorted(set(input)))
        if len(input) == 2:
            wires[hash] = 1
        elif len(input) == 7:
            wires[hash] = 8
        elif len(input) == 3:
            wires[hash] = 7
        elif len(input) == 4:
            wires[hash] = 4
        else:
            continue
        wires_reverse[wires[hash]] = set(input)

    for input in inputs:
        hash = ''.join(sorted(set(input)))
        if hash in wires:
            continue

        # It’s a 2, 3 or 5
        if len(input) == 5:
            # if it’s similar to a 1, it’s a 3
            if wires_reverse[1].issubset(set(input)):
                wires[hash] = 3
                wires_reverse[3] = set(input)

            # if it’s 1 missing from a 4, it’s a 5
            elif len(wires_reverse[4] - set(input)) == 1:
                wires[hash] = 5
                wires_reverse[5] = set(input)

            # otherwise it’s a 2
            else:
                wires[hash] = 2
                wires_reverse[2] = set(input)

    for input in inputs:
        hash = ''.join(sorted(set(input)))
        if hash in wires:
            continue

        # It’s a 0, 6 or 9
        if len(input) == 6:
            # if it’s similar to a 3, it’s a 9
            if wires_reverse[3].issubset(set(input)):
                wires[hash] = 9
                wires_reverse[9] = set(input)

            # if it’s 1 missing from a 5, it’s a 6
            elif len(set(input) - wires_reverse[5]) == 1:
                wires[hash] = 6
                wires_reverse[6] = set(input)

            # otherwise it’s a 0
            else:
                wires[hash] = 0
                wires_reverse[0] = set(input)
    return wires


def decode(output: list[str], wires: dict[str, int]) -> int:
    return int(
        ''.join(str(wires[''.join(sorted(set(digit)))]) for digit in output)
    )


def part2(data: list[tuple[list[str], list[str]]]) -> int:
    out = []
    for input, output in data:
        wires = rewire(input)
        out.append(decode(output, wires))
    print(out)
    return sum(out)


if __name__ == '__main__':
    mydata = data_import('data/y2021/day8', split_char='|')
    # mydata = data_import('data/y2021/day8_example', split_char='|')

    mydata = convert(mydata)

    print('Input is', mydata)

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
