import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
E = [int(input_()) for _ in range(N)]
ps = [0]
for i in range(N):
    ps.append(ps[-1] + E[i])

# dp[i] = (i번째 소까지만 있다고 가정할 때 최댓값)
dp = [0] * (N + 1)
dp[0] = 0
dq = deque()
dq.append((0, 0))
for i in range(1, N + 1):
    while dq and dq[0][1] < i - K:
        dq.popleft()
    while dq and dq[-1][0] <= dp[i - 1] - ps[i]:
        dq.pop()
    dp[i] = ps[i] + (dq[0][0] if dq else dp[i - 1] - ps[i])
    dq.append((dp[i - 1] - ps[i], i))

print(dp[-1])
