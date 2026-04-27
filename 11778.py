import sys
from math import gcd
input_ = sys.stdin.readline
mod = 10 ** 9 + 7
def minput(): return map(int, input_().split())


def matrix_mult(a, b):
    r = [[0] * len(b[0]) for _ in range(len(a))]
    for p in range(len(a)):
        for q in range(len(b[0])):
            for s in range(len(a[0])):
                r[p][q] += a[p][s] * b[s][q]
            r[p][q] %= mod
    return r


def matrix_pow(a, b):
    if b <= 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= mod
        return a
    if not b % 2:
        t = matrix_pow(a, b // 2)
        return matrix_mult(t, t)
    else:
        t = matrix_pow(a, b - 1)
        return matrix_mult(t, a)


n, m = minput()
t = matrix_pow([[1, 1], [1, 0]], gcd(m, n) - 1)
r = matrix_mult(t, [[1], [0]])
print(r[0][0])
