import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


K, N = minput()
if N == 1:
    exit(print(-1))
lo = -1
hi = 10 ** 18 + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if mid < K or (mid - K) * N < mid:
        lo = mid
    else:
        hi = mid

print(hi)
