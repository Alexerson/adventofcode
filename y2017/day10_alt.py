from functools import reduce
from itertools import accumulate, zip_longest as zipl
from operator import mul, xor


def reverse_sublist(l, a, b):
    if a <= b:
        l[a:b] = l[a:b][::-1]
    else:
        r = (l[a:] + l[:b])[::-1]
        l[a:], l[:b] = r[: len(l) - a], r[-b or len(r) :]


def hash_round(
    lens, elems, pos=0, skip=0, accumulator=lambda x, y: (y[0], reduce(sum, x))
):
    for (skip, s), pos in accumulate(
        zipl(enumerate(lens, skip), [pos]), accumulator
    ):
        reverse_sublist(elems, pos % len(elems), (pos + s) % len(elems))
    return elems, skip + s + pos, skip + 1


def solve1(input, n=256):
    return mul(
        *hash_round([int(l) for l in input.split(',')], list(range(n)))[0][:2]
    )


def solve2(
    input, n=256, g=16, rounds=64, suffix=[17, 31, 73, 47, 23], pos=0, skip=0
):
    elems, lengths = [*range(n)], [ord(c) for c in input.strip()] + suffix
    for _ in range(rounds):
        elems, pos, skip = hash_round(lengths, elems, pos, skip)
    return bytes(
        reduce(xor, elems[g * k : g * (k + 1)]) for k in range(n // g)
    ).hex()
