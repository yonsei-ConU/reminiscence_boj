import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, x = minput()
dp = [[0] * (x + 1) for _ in range(N + 1)]
for t in range(N):
    L, C = minput()
    for i in range(x + 1):
        if dp[t][i]:
            for j in range(i, min(i + C * L + 1, x + 1), L):
                dp[t+1][j] += dp[t][i]
    for i in range(L, min(C * L + 1, x + 1), L):
        dp[t+1][i] += 1

print(dp[-1][-1])
