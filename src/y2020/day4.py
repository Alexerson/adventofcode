import string
from typing import Any, Dict, List


def data_import(filename):
    data = []
    with open(filename, encoding='utf-8') as file:
        line = file.readline()

        item = []

        while line:
            line = line.strip()
            if line == '':
                data.append(dict(sorted(item)))
                item = []
            for keyvalue in line.split(' '):
                if ':' in keyvalue:
                    key, value = keyvalue.split(':')
                    item.append((key, value))
            line = file.readline()

        data.append(dict(sorted(item)))

    keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid',
    ]

    for key in keys[::-1]:
        data.sort(key=lambda a: a.get(key, ''))

    return data


def part1(data: List[Dict[str, Any]]):
    needed_keys = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # "cid",
    }

    valids = []
    for item in data:
        try:
            for key in needed_keys:
                item[key]
        except KeyError:
            continue
        else:
            valids.append(item)

    return len(valids)


def is_valid_byr(item):
    try:
        byr = item['byr']
    except KeyError:
        return False
    if len(byr) != 4:
        return False
    try:
        byr = int(byr)
    except ValueError:
        return False
    return 1920 <= byr <= 2002


def is_valid_iyr(item):
    try:
        iyr = item['iyr']
    except KeyError:
        return False
    if len(iyr) != 4:
        return False
    try:
        iyr = int(iyr)
    except ValueError:
        return False
    return 2010 <= iyr <= 2020


def is_valid_eyr(item):
    try:
        eyr = item['eyr']
    except KeyError:
        return False
    if len(eyr) != 4:
        return False
    try:
        eyr = int(eyr)
    except ValueError:
        return False
    return 2020 <= eyr <= 2030


def is_valid_hgt(item):
    try:
        hgt = item['hgt']
    except KeyError:
        return False

    if hgt.endswith('cm'):
        hgt = int(hgt[:-2])
        return 150 <= hgt <= 193

    if hgt.endswith('in'):
        hgt = int(hgt[:-2])
        return 59 <= hgt <= 76

    return False


def is_valid_hcl(item):
    try:
        hcl = item['hcl']
    except KeyError:
        return False

    if len(hcl) != 7:
        return False

    if hcl[0] != '#':
        return False

    return all(char in set('0123456789abcdef') for char in hcl[1:])


def is_valid_ecl(item):
    try:
        ecl = item['ecl']
    except KeyError:
        return False

    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_valid_pid(item):
    try:
        pid = item['pid']
    except KeyError:
        return False
    if len(pid) != 9:
        return False
    return all(item in set(string.digits) for item in pid)


def part2(data: List[Dict[str, Any]]):
    validations = [
        is_valid_byr,
        is_valid_iyr,
        is_valid_eyr,
        is_valid_hgt,
        is_valid_hcl,
        is_valid_ecl,
        is_valid_pid,
    ]

    valid = [
        item
        for item in data
        if all(validation(item) for validation in validations)
    ]

    return len(valid)


if __name__ == '__main__':
    mydata = data_import('data/y2020/day4')
    print('Input is', mydata)
    print('Input length is', len(mydata))
    print('Solution of 1 is', part1(mydata))
    print('Solution of 2 is', part2(mydata))
