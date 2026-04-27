import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


d, n, m = minput()
dolsum = [int(input_()) for _ in range(n)]
dolsum = sorted(dolsum) + [d]
lo = 0
hi = d + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    cur = 0
    removed = 0
    for pos in dolsum:
        if pos - cur < mid:
            removed += 1
        else:
            cur = pos
    if removed <= m:
        lo = mid
    else:
        hi = mid

print(lo)
