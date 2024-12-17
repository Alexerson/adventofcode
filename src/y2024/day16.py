from dataclasses import dataclass
from time import sleep

from utils import data_import, assert_result


@dataclass
class Maze:
    start: tuple[int, int]
    end: tuple[int, int]
    walls: set[tuple[int, int]]

    @classmethod
    def from_data(cls, data: list[str]) -> 'Maze':
        start: tuple[int, int] | None = None
        end: tuple[int, int] | None = None
        walls: set[tuple[int, int]] = set()

        for row_no, row in enumerate(data):
            for column_no, cell in enumerate(row):
                if cell == '#':
                    walls.add((column_no, row_no))
                elif cell == 'S':
                    start = (column_no, row_no)
                elif cell == 'E':
                    end = (column_no, row_no)

        return cls(start=start, end=end, walls=walls)

    def solve(
        self,
    ) -> tuple[
        int,
        list[list[tuple[int, int]]],
    ]:
        scores: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}
        best_path_to: dict[
            tuple[tuple[int, int], tuple[int, int]],
            list[set[tuple[int, int]]],
        ] = {(self.start, (1, 0)): [[self.start]]}
        to_test = {(self.start, (1, 0), 0)}

        while to_test:
            position, orientation, score = to_test.pop()

            # turn left
            orientation_left = (orientation[1], -orientation[0])
            orientation_right = (-orientation[1], orientation[0])
            score_with_turn = score + 1000
            new_position = (
                position[0] + orientation[0],
                position[1] + orientation[1],
            )
            score_straight = score + 1

            new_options = [
                (position, orientation_left, score_with_turn),
                (position, orientation_right, score_with_turn),
                (new_position, orientation, score_straight),
            ]

            for position_test, orientation_test, new_score in new_options:
                if position_test in self.walls:
                    continue

                # We never tested that, or it's at least as good as what we already did:
                if (
                    position_test,
                    orientation_test,
                ) not in scores or new_score <= scores[
                    position_test, orientation_test
                ]:
                    # If it's an absolute best, we have only one path to it:
                    if (
                        scores.get((position_test, orientation_test))
                        != new_score
                    ):
                        best_path_to[position_test, orientation_test] = []
                    to_test.add((
                        position_test,
                        orientation_test,
                        new_score,
                    ))
                    scores[position_test, orientation_test] = new_score

                    for existing_path_to_position in best_path_to[
                        position, orientation
                    ]:
                        new_path = {
                            *existing_path_to_position,
                            position_test,
                        }
                        if (
                            new_path
                            not in best_path_to[
                                position_test, orientation_test
                            ]
                        ):
                            best_path_to[
                                position_test, orientation_test
                            ].append(new_path)

        possible_configurations = [
            (self.end, (0, 1)),
            (self.end, (1, 0)),
            (self.end, (0, -1)),
            (self.end, (-1, 0)),
        ]

        best_score = min(scores[config] for config in possible_configurations)
        best_score_configs = [
            config
            for config in possible_configurations
            if scores[config] == best_score
        ]

        best_paths = []
        for config in best_score_configs:
            best_paths += best_path_to[config]

        return best_score, best_paths


def part1(data: list[str]) -> int:
    maze = Maze.from_data(data)
    return maze.solve()[0]


def part2(data: list[str]) -> int:
    maze = Maze.from_data(data)
    best_paths_to = maze.solve()[1]
    in_best_path = set()

    for path in best_paths_to:
        in_best_path |= set(path)
    return len(in_best_path)


if __name__ == '__main__':
    example = data_import('data/y2024/day16-example')
    mydata = data_import('data/y2024/day16')

    #    assert_result(part1(example), 7036)
    #    print('Solution of 1 is', part1(mydata))  # 9 min
    assert_result(part2(example), 45)
    print('Solution of 2 is', part2(mydata))  # 35 min
