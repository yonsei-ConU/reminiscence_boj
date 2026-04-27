import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

mod = 1000000007
N, M = minput()
dp = [[0] * 26 for _ in range(M)]
dp[0] = [1] * 26

for x in range(1, M):
    for i in range(26):
        for j in range(26):
            if abs(i - j) >= N:
                dp[x][i] += dp[x-1][j]
        dp[x][i] %= mod

print(sum(dp[-1]) % mod)
