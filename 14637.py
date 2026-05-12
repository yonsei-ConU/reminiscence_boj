import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, t = minput()
j = [list(minput()) for _ in range(n)]

lo = -min(si for di, si in j)
hi = 100000000.01
for i in range(10000):
    mid = (lo + hi) / 2
    cur_time = sum(di / (si + mid) for di, si in j)
    if cur_time < t:
        hi = mid
    else:
        lo = mid

print(mid)
