import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
A = list(minput())
# dp[i][j][k] = (i번째 그룹까지, j번 사이즈 변경, 현재 구간의 시작이 k) -> 직전 구간까지의 wasted
dp = [[[1 << 30] * N for _ in range(K + 1)] for __ in range(N)]
dp[0][0][0] = 0

for i in range(1, N):
    ...
