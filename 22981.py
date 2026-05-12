import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
V = sorted(list(minput()))
ans = 10 ** 20
for p in range(1, N):
    v1 = V[0] * p
    v2 = V[p] * (N - p)
    lo = 0
    hi = K // min(v1, v2) + 2
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if (v1 + v2) * mid >= K: hi = mid
        else: lo = mid
    ans = min(ans, hi)
print(ans)
