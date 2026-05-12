# 5m 10.18s

import sys
from fractions import Fraction
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, m = minput()
    seq = [-1] * n
    for __ in range(m):
        x, y = minput()
        seq[x - 1] = y
    if seq[0] == seq[1] == -1:
        seq[0] = seq[1] = 100
    elif seq[0] == -1:
        seq[0] = 100
    elif seq[1] == -1:
        seq[1] = seq[0]
    cur = 0
    for i in range(2, n)[::-1]:
        if seq[i] == -1:
            seq[i] = cur
        else:
            cur = seq[i]

    nu = seq[0] + seq[1]
    de = sum(seq)
    if not nu % de:
        nu //= gcd(nu, de)
        print(f"{nu}/1")
    else:
        print(Fraction(nu, de))
