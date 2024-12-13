from dataclasses import dataclass

from src.utils import assert_result, data_import


class NoSolutionError(Exception):
    pass


@dataclass
class Machine:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]

    @classmethod
    def get_from_data(cls, data: list[str], drift: int = 0) -> 'Machine':
        button_a = data[0].split(': ')[1]
        xa, ya = button_a.split(', ')
        button_b = data[1].split(': ')[1]
        xb, yb = button_b.split(', ')
        prize = data[2].split(': ')[1]
        xp, yp = prize.split(', ')

        return cls(
            (int(xa[1:]), int(ya[1:])),
            (int(xb[1:]), int(yb[1:])),
            (int(xp[2:]) + drift, int(yp[2:]) + drift),
        )

    def get_best_move(self) -> tuple[int, int]:
        # We need to solve:
        # n * xa + m * xb = xp
        # n * ya + m * yb = yp

        # So:
        # n = (xp - xb * m) / xa
        # (xp - xb * m) * ya / xa + m * yb =yp
        # (xp - xb * m) * ya + m * yb * xa = yp * xa
        # xp * ya - xb * ya * m + m * yb * xa = yp * xa
        # m * (yb * xa - xb * ya) = yp * xa - xp * ya
        # n = (xp * yb - yp * xb) / (xa * yb - ya * xb)
        # m = (yp * xa - xp * ya) / (yb * xa - xb * ya)

        n = (self.prize[0] * self.b[1] - self.prize[1] * self.b[0]) / (
            self.a[0] * self.b[1] - self.a[1] * self.b[0]
        )
        m = (self.prize[1] * self.a[0] - self.prize[0] * self.a[1]) / (
            self.a[0] * self.b[1] - self.a[1] * self.b[0]
        )

        # We have a valid solution only for an integer number of moves
        if n == int(n) and m == int(m):
            return int(n), int(m)

        raise NoSolutionError

    def get_best_move_cost(self) -> int:
        try:
            a, b = self.get_best_move()
        except NoSolutionError:
            return 0
        return a * 3 + b


def convert_to_machine(data: list[str], drift: int = 0) -> list[Machine]:
    machines: list[Machine] = []

    # split in chunks of 4
    machines.extend(
        Machine.get_from_data(data[i : i + 3], drift=drift)
        for i in range(0, len(data), 3)
    )

    return machines


def part1(data: list[str]) -> int:
    machines = convert_to_machine(data)
    return sum(machine.get_best_move_cost() for machine in machines)


def part2(data: list[str]) -> int:
    machines = convert_to_machine(data, drift=10000000000000)
    return sum(machine.get_best_move_cost() for machine in machines)


if __name__ == '__main__':
    example = data_import('data/y2024/day13-example')
    mydata = data_import('data/y2024/day13')

    assert_result(part1(example), 480)
    print('Solution of 1 is', part1(mydata))  # 14 min
    print('Solution of 2 is', part2(mydata))  # 16 min
