import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, Q = minput()
a = list(minput())
for _ in range(Q):
    x, y = minput()
    lo = -1
    hi = N
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            hi = mid
        else:
            lo = mid
    cannot_remove = N - hi
    print(max(0, hi - y + a[y - 1] - x + 1))
