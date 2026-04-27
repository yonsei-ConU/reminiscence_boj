import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


seq = list(minput())
dp = [[[float('inf')] * 5 for i in range(5)] for j in range(len(seq))]
dp[0][0][0] = 0

for i in range(1, len(seq)):
    nxt = seq[i - 1]
    assert nxt
    for j in range(5):
        for k in range(5):
            if not k:
                dp[i][j][nxt] = min(dp[i][j][nxt], dp[i - 1][j][k] + 2)
            else:
                x = abs(nxt - k)
                dp[i][j][nxt] = min(dp[i][j][nxt], dp[i - 1][j][k] + 5 - (x - 2) ** 2 - bool(x))
            if not j:
                dp[i][nxt][k] = min(dp[i][nxt][k], dp[i - 1][j][k] + 2)
            else:
                x = abs(nxt - j)
                dp[i][nxt][k] = min(dp[i][nxt][k], dp[i - 1][j][k] + 5 - (x - 2) ** 2 - bool(x))

ans = float('inf')
for j in range(5):
    for k in range(5):
        ans = min(ans, dp[-1][j][k])

print(ans)
