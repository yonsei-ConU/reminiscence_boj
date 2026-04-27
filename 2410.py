import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
dp = [[0] * N.bit_length() for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(N.bit_length()):
        t = i - (1 << j)
        if t < 0:
            break
        for k in range(j + 1):
            dp[i][j] += dp[t][k]
            if dp[i][j] >= 10 ** 9:
                dp[i][j] -= 10 ** 9

print(sum(dp[N]) % 10 ** 9)
