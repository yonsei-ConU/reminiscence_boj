import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
s = list(minput())
# dp[i][j] = (i번 원소에서 시작했을 때 j번만에 마지막 원소에 도달하는 확률)
dp = [[0] * n for _ in range(n)]
dp[n - 1][1] = 1
