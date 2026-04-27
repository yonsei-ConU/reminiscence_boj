import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


INF = 20202020
N = int(input_())
costs = [list(minput()) for _ in range(N)]
dp = [[INF] * N for _ in range(N)]
dp[0][1] = costs[0][1]
dp[1][0] = costs[1][0]

for i in range(2, N):
    tmp = INF
    for j in range(i - 1):
        dp[i][j] = dp[i - 1][j] + costs[i][i - 1]
        tmp = min(tmp, dp[j][i - 1] + costs[i][j])
    dp[i][i - 1] = tmp

    tmp = INF
    for j in range(i - 1):
        dp[j][i] = dp[j][i - 1] + costs[i - 1][i]
        tmp = min(tmp, dp[i - 1][j] + costs[j][i])
    dp[i - 1][i] = tmp

ans = INF
for i in range(N - 1):
    ans = min(ans, dp[-1][i], dp[i][-1])

print(ans)
