import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10 ** 9 + 7
comb = [[0] * 500 for _ in range(500)]
for i in range(500):
    comb[i][0] = 1
    comb[i][i] = 1

for n in range(1, 500):
    for r in range(1, n):
        comb[n][r] = (comb[n - 1][r - 1] + comb[n - 1][r]) % MOD

H, W = minput()
dp = [[0] * (W + 1) for _ in range(H + 1)]
dp[0][1] = 1
for i in range(H):
    for prev in range(1, W + 1):
        for nxt in range(1, W + 1):
            dp[i + 1][nxt] = (dp[i + 1][nxt] + dp[i][prev] * comb[nxt + prev - 1][nxt]) % MOD

print(sum(dp[H][:W + 1]))
