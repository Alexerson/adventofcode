from functools import reduce
from itertools import accumulate
from itertools import zip_longest as zipl
from operator import mul, xor


def reverse_sublist(list_, a, b):
    if a <= b:
        list_[a:b] = list_[a:b][::-1]
    else:
        r = (list_[a:] + list_[:b])[::-1]
        list_[a:], list_[:b] = r[: len(list_) - a], r[-b or len(r) :]


def hash_round(
    lens,
    elems,
    pos=0,
    skip=0,
    accumulator=lambda x, y: (y[0], reduce(sum, x)),
):
    for (_skip, s), pos_ in accumulate(
        zipl(enumerate(lens, skip), [pos]), accumulator
    ):
        reverse_sublist(elems, pos_ % len(elems), (pos_ + s) % len(elems))
    return elems, skip + s + pos, skip + 1


def solve1(data, n=256):
    return mul(
        *hash_round(
            [int(length) for length in data.split(',')], list(range(n))
        )[0][:2],
    )


def solve2(data, n=256, g=16, rounds=64, suffix=None, pos=0, skip=0):
    if suffix is None:
        suffix = [17, 31, 73, 47, 23]
    elems, lengths = [*range(n)], [ord(c) for c in data.strip()] + suffix
    for _ in range(rounds):
        elems, pos, skip = hash_round(lengths, elems, pos, skip)
    return bytes(
        reduce(xor, elems[g * k : g * (k + 1)]) for k in range(n // g)
    ).hex()
