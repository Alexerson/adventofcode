from typing import Dict, List

from adventofcode.utils import data_import


def part1(data: List[int]) -> int:

    jumps: Dict[int, int] = {}
    current_joltage = 0
    target_joltage = max(data) + 3

    for device_joltage in sorted(data) + [target_joltage]:
        jump = device_joltage - current_joltage
        if jump < 4:
            jumps[jump] = jumps.get(jump, 0) + 1
            current_joltage = device_joltage

    return jumps.get(1, 0) * jumps.get(3, 0)


def part2(data: List[int]) -> int:

    target_joltage = max(data) + 3

    paths = {joltage: 0 for joltage in sorted(data + [0, target_joltage])}
    paths[0] = 1

    for joltage in sorted(data) + [target_joltage]:
        for surge in (1, 2, 3):
            if joltage - surge in paths:
                paths[joltage] += paths.get(joltage - surge, 0)

    return paths[target_joltage]


if __name__ == '__main__':
    mydata = data_import('data/y2020/day10', cast=int)
    print(
        'Input is', mydata[:10], '... Min-Max: ', min(mydata), '-', max(mydata)
    )
    print('Input length is', len(mydata))

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
