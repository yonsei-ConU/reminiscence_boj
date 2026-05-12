import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
dp = [[[0] * (N + 1) for _ in range(N + 1)] for __ in range(N + 1)]
dp[1][0][0] = -1

for i in range(1, N + 1):
    for j in range(i + 1):
        for k in range(j + 1):
            dp[i][j][k] = -1
            for ni in range(1, i):
                # 첫줄을 i개만 남기고 없앰
                nxt = dp[ni][min(j, ni)][min(k, ni)]
                if nxt < 0:  # 다음상태가 지는 상태이므로 내가 이김
                    dp[i][j][k] = max(dp[i][j][k], -nxt + 1)
                elif dp[i][j][k] < 0:  # 최대한 늦게 져야 함
                    dp[i][j][k] = min(dp[i][j][k], -nxt - 1)
            for nj in range(j):
                nxt = dp[i][nj][min(k, nj)]
                if nxt < 0:
                    dp[i][j][k] = max(dp[i][j][k], -nxt + 1)
                elif dp[i][j][k] < 0:
                    dp[i][j][k] = min(dp[i][j][k], -nxt - 1)
            for nk in range(k):
                nxt = dp[i][j][nk]
                if nxt < 0:
                    dp[i][j][k] = max(dp[i][j][k], -nxt + 1)
                elif dp[i][j][k] < 0:
                    dp[i][j][k] = min(dp[i][j][k], -nxt - 1)

print(dp[N][N][N])
