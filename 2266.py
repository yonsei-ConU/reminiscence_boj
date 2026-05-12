import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
# dp[i][j]: n, k에 대한 정답
dp = [[float('inf')] * (K + 1) for _ in range(N + 1)]
for n in range(N + 1):
    dp[n][1] = n
    dp[n][0] = 0
for k in range(K + 1):
    dp[1][k] = 1
    dp[0][k] = 0

for i in range(2, N + 1):
    for j in range(2, K + 1):
        tmp = 9534781204622345789
        for a in range(i):
            b = i - 1 - a
            tmp = min(tmp, max(dp[a][j], dp[b][j - 1]))
        dp[i][j] = tmp + 1

print(dp[N][K])
