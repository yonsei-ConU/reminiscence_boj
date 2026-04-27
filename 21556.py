import sys
from bisect import bisect_left as bsl
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = N * (N - 1) // 2
med = (S + 1) >> 1
A = sorted(list(minput()))
lo = A[0] + A[1] - 1
hi = A[-1] + A[-2] + 1

while lo + 1 < hi:
    mid = (lo + hi) >> 1
    # mid 보다 작은 이익의 개수?
    s = 0
    for idx_left in range(N - 1):
        idx_right = bsl(A, mid - A[idx_left])
        s += max(idx_right - idx_left - 1, 0)
    if s < med:
        lo = mid
    else:
        hi = mid

print(lo)
