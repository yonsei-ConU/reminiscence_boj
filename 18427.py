import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

mod = 10007
N, M, H = minput()
dp = [[0] * (H + 1) for _ in range(N + 1)]
for i in range(N):
    block = [0] + list(minput())
    for h in range(H + 1):
        if dp[i][h]:
            for b in block:
                if h + b <= H:
                    dp[i + 1][h + b] += dp[i][h]
                    dp[i + 1][h + b] %= mod
    for b in block[1:]:
        if b <= H:
            dp[i + 1][b] += 1
            dp[i + 1][b] %= mod

print(dp[-1][-1] % mod)
