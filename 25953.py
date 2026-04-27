import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, t, m = minput()
start, end = minput()
tg = [[[] for _ in range(n)] for _ in range(t)]

for time in range(t):
    for _ in range(m):
        u, v, w = minput()
        tg[time][u].append((v, w))
        tg[time][v].append((u, w))

# dp[i][j]: 시간i, 정점j
dp = [[10 ** 8] * n for _ in range(t + 1)]
dp[0][start] = 0

for i in range(1, t + 1):
    for j in range(n):
        dp[i][j] = dp[i - 1][j]
        for prev, weight in tg[i - 1][j]:
            dp[i][j] = min(dp[i][j], dp[i - 1][prev] + weight)

print(dp[-1][end] if dp[-1][end] != 10 ** 8 else -1)
