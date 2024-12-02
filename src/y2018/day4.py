import operator
from datetime import datetime, timedelta

from utils import data_import


def convert_data(data):
    data = sorted(data)
    shifts = {}
    for item in data:
        date = item[1:17]
        date_parsed = datetime.strptime(date, '%Y-%m-%d %H:%M')
        event = item[19:]

        if event[:5] == 'Guard' and event[-12:] == 'begins shift':
            guard_id = event[7:-13]

        elif event == 'falls asleep':
            start_sleep = date_parsed

        elif event == 'wakes up':
            end_sleep = date_parsed
            if guard_id not in shifts:
                shifts[guard_id] = []
            shifts[guard_id].append((start_sleep, end_sleep))

    return shifts


def most_asleep(data):
    time_asleep = []
    for guard_id, shifts in data.items():
        time = sum((b - a for a, b in shifts), timedelta(0))
        time_asleep.append((guard_id, time))

    return max(time_asleep, key=operator.itemgetter(1))[0]


def most_slept_minute(shifts):
    minutes = {}
    for shift in shifts:
        for minute in range(shift[0].minute, shift[1].minute):
            if minute not in minutes:
                minutes[minute] = 0
            minutes[minute] += 1

    return max(minutes.items(), key=operator.itemgetter(1))[0]


def part1(shifts):
    guard_id = most_asleep(shifts)
    minute = most_slept_minute(shifts[guard_id])
    return (guard_id, minute, int(guard_id) * minute)


def part2(data):
    minutes = {}
    for guard_id, shifts in data.items():
        for shift in shifts:
            for minute in range(shift[0].minute, shift[1].minute):
                key = f'{guard_id}-{minute}'
                if key not in minutes:
                    minutes[key] = 0
                minutes[key] += 1

    max_key = max(minutes.items(), key=operator.itemgetter(1))[0]
    guard_id, minute = max_key.split('-')
    return (guard_id, minute, int(guard_id) * int(minute))


if __name__ == '__main__':
    data = data_import('data/day4')
    shifts = convert_data(data)
    print('Solution of 1 is', part1(shifts))
    print('Solution of 2 is', part2(shifts))
