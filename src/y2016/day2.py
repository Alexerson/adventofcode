from src.utils import assert_result, data_import


def part1(data: list[str]) -> str:
    current_digit = 5
    output = ''
    for line in data:
        for char in line:
            if char == 'U' and current_digit > 3:
                current_digit -= 3
            elif char == 'D' and current_digit < 7:
                current_digit += 3
            elif char == 'L' and current_digit % 3 != 1:
                current_digit -= 1
            elif char == 'R' and current_digit % 3 != 0:
                current_digit += 1
        output += str(current_digit)

    return output


def part2(data: list[str]) -> int:
    return len(data)


if __name__ == '__main__':
    example = data_import('data/y2016/day2-example')
    mydata = data_import('data/y2016/day2')

    assert_result(part1(example), '1985')
    print('Solution of 1 is', part1(mydata))  # 27 min 03

    assert_result(part2(example), 80)
    print('Solution of 2 is', part2(mydata))  # Paused at 32:47  x min y
