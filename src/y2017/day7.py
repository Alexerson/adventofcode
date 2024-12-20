import collections

from src.utils import data_import


def build_tree(data):
    towers = {}
    parents = {}

    for item in data:
        name = item[0]
        weight = int(item[1][1:-1])
        leafs = [a.strip(',') for a in item[3:]]

        towers[name] = {'name': name, 'weight': weight, 'leafs': leafs}

        for item in leafs:
            parents[item] = name

    return towers, parents


def get_root(parents):
    leaf = next(iter(parents.keys()))
    while leaf in parents:
        leaf = parents[leaf]
    return leaf


def part1(data):
    _towers, parents = build_tree(data)
    return get_root(parents)


def weight(key, towers):
    if 'total_weight' in towers[key]:
        return towers[key]['total_weight']

    total_weight = towers[key]['weight'] + sum(
        weight(leaf, towers) for leaf in towers[key]['leafs']
    )
    towers[key]['total_weight'] = total_weight
    return total_weight


def get_unbalanced(node, towers):
    leafs = towers[node]['leafs']
    if not leafs:
        return None

    weights = [(leaf, weight(leaf, towers)) for leaf in towers[node]['leafs']]
    counts = collections.Counter(item[1] for item in weights)

    if len(counts) == 1:
        return None

    normal = counts.most_common()[0][0]
    outliar = next((leaf, wei) for leaf, wei in weights if wei != normal)

    if towers[outliar[0]]['leafs']:
        unbalanced = get_unbalanced(outliar[0], towers)

        if unbalanced:
            return unbalanced

    return (towers[outliar[0]], normal)


def part2(data):
    towers, parents = build_tree(data)
    root = get_root(parents)

    return get_unbalanced(root, towers)


if __name__ == '__main__':
    data = data_import('data/y2017/day7_real', cast=str, split_char=' ')

    print('Solution of 1 is', part1(data))

    outliar_node, normal = part2(data)

    correct_weight = (
        outliar_node['weight'] - outliar_node['total_weight'] + normal
    )

    print(
        'Solution of 2 is:',
        correct_weight,
        f'(instead of {outliar_node["weight"]}: '
        f'total weight of this node is {outliar_node["total_weight"]} '
        f'when it should be {normal})',
    )
