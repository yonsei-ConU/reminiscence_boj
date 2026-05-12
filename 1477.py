import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, L = minput()
gbrpth = [0] + (sorted(list(minput())) if N else []) + [L]

lo = 0
hi = 1000 // M + 2
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if sum((gbrpth[i + 1] - gbrpth[i] - 1) // mid for i in range(N + 1)) <= M:
        hi = mid
    else:
        lo = mid

print(hi)
