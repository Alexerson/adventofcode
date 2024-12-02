from typing import Dict, List, Set, Tuple

from src.utils import data_import


def convert_data(data: List[List[str]]) -> Dict[str, List[Tuple[int, str]]]:
    out: Dict[str, List[Tuple[int, str]]] = {}

    for item in data:
        container, contents = item
        container = container[:-5]

        out[container] = []

        for content in contents.split(','):
            count_str, color = content.strip().split(' ', maxsplit=1)

            try:
                count = int(count_str)
            except ValueError:
                count = 0

            if color.strip('.').endswith('bags'):
                color = color[:-5].strip()
            else:
                color = color[:-4].strip()

            if count > 0:
                out[container].append((count, color))

    return out


def extract_tree(data: Dict[str, List[Tuple[int, str]]]) -> Dict[str, Set]:
    out: Dict[str, Set] = {}

    for key, value in data.items():
        for _count, color in value:
            if color not in out:
                out[color] = {key}
            else:
                out[color].add(key)

    return out


def part1(tree: Dict[str, Set]) -> int:
    root = 'shiny gold'

    to_do = {root}
    done = set()

    while to_do:
        item = to_do.pop()
        done.add(item)

        to_do.update(tree.get(item) or [])

    return len(done - {root})


def part2_count(data: Dict[str, List[Tuple[int, str]]], root: str) -> int:
    out = 1

    for count, color in data[root]:
        out += count * part2_count(data, color)

    return out


def part2(data: Dict[str, List[Tuple[int, str]]]) -> int:
    # We count them all and remove the shiny gold because we want only
    # the contained count
    return part2_count(data, 'shiny gold') - 1


if __name__ == '__main__':
    mydata = convert_data(data_import('data/y2020/day7', split_char='contain'))
    # print('Input is', mydata)
    print('Input length is', len(mydata))

    mytree = extract_tree(mydata)
    # print('Tree is', mytree)

    print('Solution of 1 is', part1(mytree))
    print('Solution of 2 is', part2(mydata))
