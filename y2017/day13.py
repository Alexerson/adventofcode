from utils import data_import


def part1(data, delay=0, penality=0):
    buckets_size = dict(data)
    buckets = {key: 2 * (buckets_size[key] - 1) for key in buckets_size}
    firewall_positions = {}

    time = max(buckets.keys())

    score = 0

    for bucket, size in buckets.items():
        firewall_positions[bucket] = delay
        firewall_positions[bucket] %= size

    for position in range(time + 1):

        if firewall_positions.get(position) == 0:
            score += penality + position * (buckets_size[position])

        for bucket, size in buckets.items():
            firewall_positions[bucket] += 1
            firewall_positions[bucket] %= size

    return score


def part2(data):
    buckets_size = dict(data)
    buckets = {key: 2 * (buckets_size[key] - 1) for key in buckets_size}
    firewall_positions = {}

    buckets_count = len(buckets.keys())

    for bucket, size in buckets.items():
        firewall_positions[bucket] = bucket % size

    delay = 0
    while True:
        total = sum(
            (firewall_positions[bucket] + delay) % buckets[bucket] != 0
            for bucket in buckets.keys()
        )

        if total == buckets_count:
            return delay
        delay += 1


if __name__ == '__main__':
    data = data_import('2017/data/day13_example', int, ':')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))

    data = data_import('2017/data/day13', int, ':')
    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
