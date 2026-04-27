import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, K = minput()
a = list(minput())
# dp[i][j]: i번째까지, 감소하는 인덱스의 개수가 j개
dp = [[1] * (K + 1) for _ in range(n)]
for i in range(n):
    t = a[i]
    for j in range(i):
        if a[j] <= t:
            for k in range(K + 1):
                dp[i][k] = max(dp[i][k], dp[j][k] + 1)
        else:
            for k in range(1, K + 1):
                dp[i][k] = max(dp[i][k], dp[j][k - 1] + 1)

print(max(dp[-1]))
