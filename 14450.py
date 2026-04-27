import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
# dp[i][j][k]: i+1 games, j times changed, last is k
dp = [[[0, 0, 0] for _ in range(K + 1)] for __ in range(N)]
gesture = input_().strip()
if gesture == 'H':
    dp[0][0][1] = 1
elif gesture == 'P':
    dp[0][0][2] = 1
else:
    dp[0][0][0] = 1

for i in range(1, N):
    gesture = input_().strip()
    if gesture == 'H':
        win = 1
    elif gesture == 'P':
        win = 2
    else:
        win = 0
    for j in range(K + 1):
        for k in range(3):
            dp[i][j][k] = dp[i - 1][j][k]
            if not j:
                if k == win:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + 1)
                else:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
            else:
                if k == win:
                    for kl in range(3):
                        if k != kl:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][kl] + 1)
                        else:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][kl] + 1)
                else:
                    for kl in range(3):
                        if k != kl:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][kl])
                        else:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])

print(max(dp[-1][-1]))
