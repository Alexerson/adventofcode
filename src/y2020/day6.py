from typing import List, Set


def data_import(filename: str) -> List[List[Set[str]]]:
    data = []
    with open(filename) as file:
        line = file.readline()

        group: List[Set[str]] = []

        while line:
            line = line.strip()
            if line == '':
                data.append(group)
                group = []
            else:
                group.append(set(line))
            line = file.readline()

        data.append(group)

    return data


def part1(data: List[List[Set[str]]]) -> int:
    return sum(len(set.union(*group)) for group in data)


def part2(data: List[List[Set[str]]]) -> int:
    return sum(len(set.intersection(*group)) for group in data)


if __name__ == '__main__':
    mydata = data_import('data/y2020/day6')
    # print('Input is', mydata)
    print('Input length is', len(mydata))
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
