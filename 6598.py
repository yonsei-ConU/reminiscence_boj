import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = max(g[i][k] * g[k][j], g[i][j])
    return g


tc = 1
while True:
    n = int(input_())
    if not n: break
    currency = {}
    for i in range(n):
        c = input_().rstrip()
        currency[c] = i
    m = int(input_())
    g = [[0] * n for _ in range(n)]
    for _ in range(m):
        c1, mult, c2 = input_().split()
        c1 = currency[c1]
        c2 = currency[c2]
        f = Fraction(mult)
        f_inv = Fraction(1) / f
        g[c2][c1] = max(g[c2][c1], f_inv)
        g[c1][c2] = max(g[c1][c2], f)
    g = floyd_warshall(g, n)
    input_()
    print(g)
