import sys
from bisect import bisect_right as upper_bound
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K, Q = minput()
min_heights = list(minput())
grow_data = list(minput())
grow = [[] for _ in range(N)]
for i in range(K):
    grow[grow_data[i] - 1].append(i)

ans = [0] * K
for _ in range(Q):
    i, j, k = minput()
    i -= 1; j -= 1
    lo = -1
    hi = K
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if upper_bound(grow[i], mid) + upper_bound(grow[j], mid) >= min_heights[k - 1]:
            hi = mid
        else:
            lo = mid
    if hi != K:
        ans[hi] += 1

psum = 0
for a in ans:
    psum += a
    print(psum)
