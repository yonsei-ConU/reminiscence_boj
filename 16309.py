import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, M = minput()
investments = []
for _ in range(n):
    profit, cost = minput()
    investments.append((-cost, profit))

lo = -1
hi = 2147483648
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if sum(max(0, inv[0] + inv[1] * mid) for inv in investments) >= M:
        hi = mid
    else:
        lo = mid

print(hi)
