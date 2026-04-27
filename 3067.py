import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

for _ in range(int(input_())):
    N = int(input_())
    values = list(minput())
    M = int(input_())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for v in range(N):
        for i in range(M + 1):
            if dp[v][i]:
                for j in range(i, M + 1, values[v]):
                    dp[v + 1][j] += dp[v][i]
        for j in range(values[v], M + 1, values[v]):
            dp[v + 1][j] += 1
    print(dp[-1][-1])
