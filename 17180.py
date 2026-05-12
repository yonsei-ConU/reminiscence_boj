import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
s1 = input_().rstrip()
s2 = input_().rstrip()

# dp[i][j] = (s1[i], s2[j]까지만 있었을 경우의 정답, 1-index)
dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        d = abs(ord(s1[i - 1]) - ord(s2[j - 1]))
        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + d

print(dp[N][M])
