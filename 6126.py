import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


V, N = minput()
values = [int(input_()) for _ in range(V)]
# dp[i][j]: i번째 동전까지 사용, 총 가치 j인 경우의 수
dp = [[0] * (N + 1) for _ in range(V + 1)]
dp[0][0] = 1

for i in range(1, V + 1):
    v = values[i - 1]
    for j in range(N + 1):
        dp[i][j] = dp[i - 1][j]
        t = j - v
        while t >= 0:
            dp[i][j] += dp[i - 1][t]
            t -= v

print(dp[V][N])
