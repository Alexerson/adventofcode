from collections import Counter

from utils import data_import


def part1(data: list[int], iterations=80) -> int:
    population = dict(Counter(data))

    for _ in range(iterations):
        new_population: dict[int, int] = {}
        for age, count in population.items():
            if age == 0:
                new_population[6] = new_population.get(6, 0) + count
                new_population[8] = count
            else:
                new_population[age - 1] = (
                    new_population.get(age - 1, 0) + count
                )

        population = new_population

    return sum(population.values())


def part2(data: list[int], iterations=256) -> int:
    return part1(data, iterations=iterations)


if __name__ == '__main__':
    mydata = data_import('y2021/data/day6', split_char=',', cast=int)[0]

    print('Input is', mydata)
    print('Solution of 1 example is', part1([3, 4, 3, 1, 2]))

    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
