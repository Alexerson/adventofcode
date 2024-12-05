import functools

from src.utils import data_import


def index_rules(
    ordering_rules: list[tuple[int, int]],
) -> dict[int, set[int]]:
    rules: dict[int, set[int]] = {}

    for before, after in ordering_rules:
        if before not in rules:
            rules[before] = set()

        rules[before].add(after)
    return rules


def reorder(pages: list[int], indexed_rules: dict[int, set[int]]) -> list[int]:
    def comparison(a: int, b: int) -> int:
        if a in indexed_rules.get(b, set()):
            return 1
        return -1

    return sorted(pages, key=functools.cmp_to_key(comparison))


def is_in_order(pages: list[int], indexed_rules: dict[int, set[int]]) -> bool:
    return pages == reorder(pages, indexed_rules)


def get_median(pages: list[int]) -> int:
    return pages[len(pages) // 2]


def part1(
    ordering_rules: list[tuple[int, int]], pages_to_produce: list[list[int]]
) -> int:
    indexed_rules = index_rules(ordering_rules)

    return sum(
        get_median(pages)
        for pages in pages_to_produce
        if is_in_order(pages, indexed_rules)
    )


def part2(
    ordering_rules: list[tuple[int, int]], pages_to_produce: list[list[int]]
) -> int:
    indexed_rules = index_rules(ordering_rules)

    return sum(
        get_median(reordered_pages)
        for pages in pages_to_produce
        if (reordered_pages := reorder(pages, indexed_rules)) != pages
    )


def extract_data(
    data: list[str],
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    ordering_rules: list[tuple[int, int]] = []
    pages_to_produce: list[list[int]] = []
    for row in data:
        if not row.strip():
            continue
        if '|' in row:
            a, b = row.split('|')
            ordering_rules.append((int(a), int(b)))
        else:
            pages_to_produce.append([int(page) for page in row.split(',')])
    return ordering_rules, pages_to_produce


if __name__ == '__main__':
    mydata = data_import('data/y2024/day5-example')
    ordering_rules, pages_to_produce = extract_data(mydata)
    assert part1(ordering_rules, pages_to_produce) == 143
    assert part2(ordering_rules, pages_to_produce) == 123

    mydata = data_import('data/y2024/day5')
    ordering_rules, pages_to_produce = extract_data(mydata)
    print('Solution of 1 is', part1(ordering_rules, pages_to_produce))
    print('Solution of 2 is', part2(ordering_rules, pages_to_produce))
