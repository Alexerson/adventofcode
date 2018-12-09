from collections import deque

from utils import data_import


def add_marble(number, circle):

    if number % 23 == 0:
        circle.rotate(7)
        score = number + circle.pop()
        circle.rotate(-1)

    else:
        score = 0
        circle.rotate(-1)
        circle.append(number)

    return circle, score


def part1(nb_players, last_marble):
    circle = deque([0, 1])

    scores = {}

    for marble in range(2, last_marble):
        circle, score = add_marble(marble, circle)
        player = marble % nb_players

        scores[player] = scores.get(player, 0) + score

    return max(scores.values())


def part2(nb_players, last_marble):
    return part1(nb_players, last_marble * 100)


if __name__ == '__main__':
    print('Solution of 1 is', part1(447, 71510))
    print('Solution of 2 is', part2(447, 71510))
