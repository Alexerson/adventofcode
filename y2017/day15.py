from utils import data_import


def generator(seed, factor, multiple=1):
    value = seed

    while True:
        value *= factor
        value %= 2147483647
        if value % multiple == 0:
            yield value


def part1(seed_a, seed_b, rounds=40000000):
    generator_a = generator(seed_a, 16807)
    generator_b = generator(seed_b, 48271)

    judge_count = 0

    for round_ in range(rounds):
        value_a = next(generator_a)
        value_b = next(generator_b)

        if value_a % 65536 == value_b % 65536:
            judge_count += 1

    return judge_count


def part2(seed_a, seed_b, rounds=5000000):
    generator_a = generator(seed_a, 16807, 4)
    generator_b = generator(seed_b, 48271, 8)

    judge_count = 0

    for round_ in range(rounds):
        value_a = next(generator_a)
        value_b = next(generator_b)

        if value_a % 65536 == value_b % 65536:
            judge_count += 1

    return judge_count


if __name__ == '__main__':
    print('Solution of 1 is', part1(65, 8921))
    print('Solution of 2 is', part2(65, 8921))

    print('Solution of 1 is', part1(783, 325))
    print('Solution of 2 is', part2(783, 325))
