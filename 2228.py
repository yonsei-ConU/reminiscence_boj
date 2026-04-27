import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
A = [int(input_()) for _ in range(N)]
# dp[i][j] = i번째 수까지 j개의 구간에 나누어 담음
dp = [[0] * (M + 1) for _ in range(N)]
dp[0][1] = A[0]

for i in range(1, N):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + A[i]
