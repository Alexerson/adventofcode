from utils import data_import
from intcode import execute
import collections
from functools import lru_cache

def convert(data):
    tree = {}
    for a, b in data:
        tree[b] = a
    return tree

def depth(item, tree):
    @lru_cache
    def depth_sub(item):
        count = 0
        while item != 'COM':
            count += 1
            item = tree[item]
        return count
    return depth_sub(item)

def part1(data):
    tree = convert(data)
    return sum(depth(item, tree) for item in tree.keys())
    

def part2(data):
    tree = convert(data)

    path_me = {}
    item = 'YOU'
    count = 0
    while item != 'COM':
        path_me[item] = count
        item = tree[item]
        count += 1

    path_santa = {}
    item = 'SAN'
    count = 0
    while item not in path_me:
        path_santa[item] = count
        item = tree[item]
        count += 1

    return path_me[item] + count - 2  # -2 because I only need to be one level deeper to change


if __name__ == '__main__':
    data = data_import('y2019/data/day6', split_char=')')
    data_example = data_import('y2019/data/day6_example', split_char=')')

    print('Solution of 1st example is', part1(data_example))
    print('Solution of 1 is', part1(data))

    data_example = data_import('y2019/data/day6_example2', split_char=')')
    print('Solution of 2nd example is', part2(data_example))
    print('Solution of 2 is', part2(data))
