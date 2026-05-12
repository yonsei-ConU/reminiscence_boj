import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
A = list(map(lambda x: int(x) % M, input_().split()))
ps = [0]
for i in range(N):
    ps.append((ps[-1] + A[i]) % M)

cnt = Counter(ps)
ans = 0
for val in cnt.values():
    ans += val * (val - 1) // 2

print(ans)
