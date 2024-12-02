import math

from utils import data_import


class Reaction:
    def __init__(self, before, after):
        self.before = before
        self.after_quantity = after[0]
        self.after_kind = after[1]

    def __str__(self):
        return (
            f'Reaction {self.before} -> {self.after_quantity}, '
            f'{self.after_kind}'
        )


def build_reactions(data):
    reactions = {}

    for reaction in data:
        before_list = []
        before, after = reaction.split('=>')

        for before_values in before.split(','):
            quantity, kind = before_values.strip().split(' ')
            before_list.append((int(quantity), kind.strip()))

        after_quantity, after_kind = after.strip().split(' ')

        reactions[after_kind.strip()] = Reaction(
            before_list,
            (int(after_quantity), after_kind.strip()),
        )

    return reactions


def compute_depths(reactions):
    depths = ['ORE']

    reactions = list(reactions.values())

    while reactions:
        reaction = reactions.pop(0)

        works = True
        for _quantity, kind in reaction.before:
            if kind not in depths:
                works = False
                break

        if works:
            depths.append(reaction.after_kind)
        else:
            reactions.append(reaction)

    return depths


def part1(data, fuel_quantity=1):
    reactions = build_reactions(data)
    depths = compute_depths(reactions)
    depths.reverse()

    possessions = {'FUEL': fuel_quantity}

    for converted_kind in depths[:-1]:
        reaction = reactions.get(converted_kind)

        times = math.ceil(
            possessions[converted_kind] / reaction.after_quantity
        )

        for quantity, kind in reaction.before:
            possessions[kind] = possessions.get(kind, 0) + times * quantity
        possessions[converted_kind] = (
            times * reaction.after_quantity - possessions[converted_kind]
        )
    return possessions['ORE']


def part2(data):
    wanted_ore_quantity = 1_000_000_000_000
    max_fuel_quantity = wanted_ore_quantity
    min_fuel_quantity = 0

    while (max_fuel_quantity - min_fuel_quantity) > 1:
        fuel_quantity = (max_fuel_quantity + min_fuel_quantity) // 2
        ore_quantity = part1(data, fuel_quantity=fuel_quantity)
        if ore_quantity > wanted_ore_quantity:
            max_fuel_quantity = fuel_quantity
        elif ore_quantity < wanted_ore_quantity:
            min_fuel_quantity = fuel_quantity
        else:
            return fuel_quantity

    return min_fuel_quantity


if __name__ == '__main__':
    data = data_import('data/y2019/day14_example0')
    print('Solution of example 1 is', part1(data))
    print('Solution of example 2 is', part2(data))

    data = data_import('data/y2019/day14')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
