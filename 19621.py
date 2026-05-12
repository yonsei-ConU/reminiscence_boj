import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ghldml = [list(minput())[2] for _ in range(N)]
dp = [0] * N
dp[0] = ghldml[0]

if N != 1: dp[1] = ghldml[1]

for i in range(2, N):
    tmp = max(dp[:i - 1]) + ghldml[i]
    dp[i] = max(tmp, dp[i - 1])

print(max(dp))
