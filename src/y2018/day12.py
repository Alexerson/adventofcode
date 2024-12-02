from utils import data_import


def convert_rules(data):
    rules = {}

    for rule in data:
        key, value = rule.split('=>')
        key = tuple(b == '#' for b in key.strip())
        rules[key] = value.strip() == '#'

    return rules


def evolve(pots, rules):
    min_index = min(pots)
    max_index = max(pots)

    new_pots = set()

    for pot in range(min_index - 2, max_index + 3):
        neighborhood = tuple(
            (pot + neighbor) in pots for neighbor in range(-2, 3)
        )

        if rules.get(neighborhood):
            new_pots.add(pot)

    return new_pots


def part1(data_input, data_rules, iterations=20):
    rules = convert_rules(data_rules)
    pots = {index for index, value in enumerate(data_input) if value == '#'}

    for _i in range(iterations):
        pots = evolve(pots, rules)

    return sum(pots)


def part2(data_input, data_rules, iterations):
    if iterations < 2000:
        return part1(data_input, data_rules, iterations)
    after_2000 = part1(data_input, data_rules, 2000)
    after_2001 = part1(data_input, data_rules, 2001)
    after_2002 = part1(data_input, data_rules, 2002)

    diff = after_2001 - after_2000
    assert diff == after_2002 - after_2001

    return (iterations - 2000) * diff + after_2000


if __name__ == '__main__':
    data = data_import('data/day12_example', str)
    print('Example:')
    print('Solution of 1 is', part1(data[0][15:], data[1:]))
    print('Solution of 2 is', part2(data[0][15:], data[1:], 50000000000))

    print('Real:')
    data = data_import('data/day12_real', str)
    print('Solution of 1 is', part1(data[0][15:], data[1:]))
    print('Solution of 2 is', part2(data[0][15:], data[1:], 50000000000))
