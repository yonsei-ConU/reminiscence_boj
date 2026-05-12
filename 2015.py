import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
A = list(minput())
ps = []
cur_sum = 0
for i in range(N):
    cur_sum += A[i]
    ps.append(cur_sum)

cnt = Counter(ps)
ans = cnt[K]

for i in range(N):
    x = ps[i]
    cnt[x] -= 1
    ans += cnt[x + K]

print(ans)
