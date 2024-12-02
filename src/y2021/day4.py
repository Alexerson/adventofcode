import contextlib
from copy import copy

from utils import data_import


class Board:
    def __init__(self, data, width=5):
        self._original = data
        self._width = width
        self._unmarked = set(data)

        self._sets = []
        for i in range(width):
            self._sets.append(set(data[i * width : (i + 1) * width]))
            self._sets.append(set(data[i::width]))

    def mark(self, value):
        try:
            self._unmarked.remove(value)
        except KeyError:
            return

        for set_ in self._sets:
            with contextlib.suppress(KeyError):
                set_.remove(value)

    def is_winner(self):
        return any(len(set_) == 0 for set_ in self._sets)


def convert(data: list[str], board_lines=5) -> tuple[list[int], list[Board]]:
    drawn_numbers = [int(x) for x in data[0].split(',')]

    boards = []

    board = []
    lines = 0
    for line in data[1:]:
        board += [int(x) for x in line.split()]
        lines += 1

        if lines == board_lines:
            boards.append(Board(board))
            board = []
            lines = 0

    return drawn_numbers, boards


def part1(drawn_numbers: list[int], boards: list[Board]) -> list[int]:
    for number in drawn_numbers:
        for board in boards:
            board.mark(number)

        winners = [board for board in boards if board.is_winner()]

        if winners:
            return [number * sum(board._unmarked) for board in winners]
    return None


def part2(drawn_numbers: list[int], boards: list[Board]) -> list[int]:
    left = copy(boards)

    for number in drawn_numbers:
        for board in left:
            board.mark(number)

        losers = [board for board in left if not board.is_winner()]

        if not losers:
            return [number * sum(board._unmarked) for board in left]

        left = losers
    return None


if __name__ == '__main__':
    # mydata = data_import('data/y2021/day4_example')
    mydata = data_import('data/y2021/day4')

    drawn_numbers, boards = convert(mydata)
    print('Input is', drawn_numbers, boards)
    print('Solution of 1 is', part1(drawn_numbers, boards))
    print('Solution of 2 is', part2(drawn_numbers, boards))
