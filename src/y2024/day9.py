from src.utils import assert_result, data_import


def part1(data: str) -> int:
    disk: list[int | None] = []

    for index, value in enumerate(data):
        length = int(value)
        if length:
            file_id = index // 2 if index % 2 == 0 else None
            disk += [file_id] * length

    while None in disk:
        value_ = disk.pop()
        if value_ is None:
            continue
        first_dot = disk.index(None)
        disk[first_dot] = value_

    return checksum(disk)


def checksum(disk: list[int | None]) -> int:
    total = 0
    for index, value in enumerate(disk):
        if value is not None:
            total += value * index
    return total


def files_to_disk(
    files: dict[int, tuple[int, int]],
) -> list[int | None]:
    biggest_index = max(index for index, _ in files.values())
    disk: list[int | None] = [None] * (biggest_index + 1)

    for file_id, (index, length) in files.items():
        disk[index : index + length] = [file_id] * length

    return disk


def part2(data: str) -> int:
    files: dict[int, tuple[int, int]] = {}
    empty_space: dict[int, list[int]] = {}

    cursor = 0
    for index, value in enumerate(data):
        length = int(value)
        if index % 2 == 0:
            file_id = index // 2
            files[file_id] = cursor, length
        else:
            if length not in empty_space:
                empty_space[length] = []
            empty_space[length].append(cursor)
        cursor += length

    for file_index in sorted(files.keys(), reverse=True):
        try:
            index, length = files[file_index]
        except KeyError:
            continue

        possible_empty_spaces = [
            (empty_space_index, empty_space_length)
            for empty_space_length in empty_space
            if empty_space_length >= length
            and empty_space[empty_space_length]
            and (empty_space_index := min(empty_space[empty_space_length]))
            < index
        ]

        if not possible_empty_spaces:
            continue

        empty_space_index, empty_space_length = min(possible_empty_spaces)
        empty_space[empty_space_length].remove(empty_space_index)

        new_empty_space = empty_space_length - length
        if new_empty_space not in empty_space:
            empty_space[new_empty_space] = []
        empty_space[new_empty_space].append(empty_space_index + length)

        files[file_index] = empty_space_index, length

    disk = files_to_disk(files)
    return checksum(disk)


if __name__ == '__main__':
    mydata = data_import('data/y2024/day9-example')[0]

    assert_result(part1(mydata), 1928)
    assert_result(part2(mydata), 2858)

    mydata = data_import('data/y2024/day9')[0]
    print('Solution of 1 is', part1(mydata))  # 20 min
    print('Solution of 2 is', part2(mydata))  # 1h03 min
