import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, a, b = minput()
dp = [2000000] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    for nxt in (j for j in [i + 1, i + a + 1, i + b + 1] if j <= N):
        dp[nxt] = min(dp[nxt], dp[i] + 1)

print(dp[-1])
