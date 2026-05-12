import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
pairs = []
for _ in range(K):
    p, q = minput()
    if p > q: p, q = q, p
    pairs.append((p, q))
pairs.sort(key=lambda x: x[1])
cur = 1
ans = 1
for x, y in pairs:
    if x < cur:
        continue
    else:
        ans += 1
        cur = y

print(ans)
