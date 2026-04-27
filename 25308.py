import sys
from itertools import permutations
from math import sqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]


r2 = 1 / sqrt(2)
ans = 0
for p in permutations(list(minput())):
    chk = 1
    for start in range(8):
        v1 = p[start]
        v2 = p[(start + 1) & 7]
        v3 = p[(start + 2) & 7]
        p1 = (v1, 0)
        p2 = (v2 * r2, v2 * r2)
        p3 = (0, v3)
        if ccw(p1, p2, p3) < 0:
            chk = 0
            break
    ans += chk

print(ans)
