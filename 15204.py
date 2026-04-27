import sys
from itertools import combinations
from math import lcm
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
A = list(minput())
pre = []

for i in range(1, N + 1):
    tmp = []
    for j in combinations(A, i):
        tmp.append(lcm(*j))
    pre.append(tmp)

for _ in range(M):
    Q = int(input_())
    lo = 0
    hi = 10 ** 18 + 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        multiple = 0
        for i in range(1, N + 1):
            for j in pre[i - 1]:
                multiple += (-1) ** (i - 1) * (mid // j)
        if multiple >= Q:
            hi = mid
        else:
            lo = mid
    print(hi)
