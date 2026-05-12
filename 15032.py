import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
# dp[i][j]: 뒤집은 횟수가 i번일 때 face-up이 j개인 경우의 수
dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1

for i in range(K):
    for j in range(N):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j + 1] += dp[i][j]
    dp[i + 1][N - 1] += dp[i][N]
    dp[i + 1][N] += dp[i][N]

print(sum(i * dp[-1][i] for i in range(N + 1)) / sum(dp[-1]))
