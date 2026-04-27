import sys
from math import ceil
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    n, s, p = minput()
    peri = 0
    x, y = minput()
    for i in range(n):
        nx, ny = minput()
        assert x == nx or y == ny
        peri += abs(x - nx) + abs(y - ny)
        x, y = nx, ny

    print(f"Data Set {tc}:")
    print(ceil(s * peri / p))
    print()
