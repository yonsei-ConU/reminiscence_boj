import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, L, I = minput()
# dp[i][j]: N자리 이진수, j개의 비트가 1 (조합...)
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][0] = dp[1][1] = 1
for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

ans = []
n = N
l = L
i = I - 1
while n:
    print(n, l, i)
    if i >= sum(dp[n - 1][:l + 1]):
        i -= sum(dp[n - 1][:l + 1])
        ans.append('1')
        l -= 1
    else:
        ans.append('0')
    n -= 1

print(''.join(ans))
