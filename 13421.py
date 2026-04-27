import sys
from itertools import permutations as P
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def calc_cost(x):
    x /= 2
    V = [(x, x), (x, -x), (-x, x), (-x, -x)]
    ret = 10 ** 18
    for perm in P(range(4)):
        cur = 0
        for i, v in enumerate(perm):
            cur += abs(first[i][0] - V[v][0]) + abs(first[i][1] - V[v][1])
        ret = min(cur, ret)
    return ret


first = [list(minput()) for _ in range(4)]
lo = 1
hi = 1000000001
while lo + 2 < hi:
    mid1 = (lo + hi) >> 1
    mid2 = mid1 + 1
    cost1 = calc_cost(mid1)
    cost2 = calc_cost(mid2)
    if cost1 < cost2:
        hi = mid2
    else:
        lo = mid1

ans = 0
best = 10 ** 18
for x in range(min(1, lo - 100), hi + 100):
    cur = calc_cost(x)
    if cur <= best:
        ans = x
        best = cur

print(ans)
