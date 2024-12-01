import collections
from collections import deque

import parse

from utils import data_import


def part1(rounds):
    elves_1 = 3
    elves_2 = 7

    all_recipes = [3, 7]

    elves_1_index = 0
    elves_2_index = 1

    while len(all_recipes) < rounds + 10:
        new_recipe = elves_1 + elves_2
        new_1 = new_recipe // 10
        new_2 = new_recipe % 10

        if new_1:
            all_recipes.append(new_1)

        all_recipes.append(new_2)

        elves_1_index += 1 + elves_1
        elves_2_index += 1 + elves_2

        elves_1_index %= len(all_recipes)
        elves_2_index %= len(all_recipes)

        elves_1 = all_recipes[elves_1_index]
        elves_2 = all_recipes[elves_2_index]

    return ''.join('{}'.format(i) for i in all_recipes[rounds : rounds + 10])


def part2(data):
    elves_1 = 3
    elves_2 = 7

    all_recipes = [3, 7]

    elves_1_index = 0
    elves_2_index = 1

    data_list = [int(i) for i in data]
    len_data = len(data)

    while True:
        new_recipe = elves_1 + elves_2
        new_1 = new_recipe // 10
        new_2 = new_recipe % 10

        if new_1:
            all_recipes.append(new_1)

        all_recipes.append(new_2)

        elves_1_index += 1 + elves_1
        elves_2_index += 1 + elves_2

        elves_1_index %= len(all_recipes)
        elves_2_index %= len(all_recipes)

        elves_1 = all_recipes[elves_1_index]
        elves_2 = all_recipes[elves_2_index]

        if (
            data_list == all_recipes[-len_data:]
            or data_list == all_recipes[-len_data - 1 : -1]
        ):
            return ''.join('{}'.format(i) for i in all_recipes).index(data)


if __name__ == '__main__':
    print('Solution of 1 for example is', part1(9))
    print('Solution of 1 for example is', part1(5))
    print('Solution of 1 for example is', part1(18))
    print('Solution of 1 for example is', part1(2018))
    print('Solution of 1 for real is', part1(864801))

    print('Solution of 2 for example is', part2("51589"))
    print('Solution of 2 for example is', part2("01245"))
    print('Solution of 2 for example is', part2("92510"))
    print('Solution of 2 for example is', part2("59414"))
    print('Solution of 2 for real is', part2("864801"))
