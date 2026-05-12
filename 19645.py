import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
a = list(minput())
s = sum(a)

# dp[i][j]: i번째 햄버거까지 처리함, 길원 효용이 j. 이때 두 선배 효용이 튜플로 들어가있음.
dp = [[(0, 0) for __ in range(s + 1)] for _ in range(N + 1)]
ans = 0

for i in range(N):
    d = a[i]
    for j in range(s):
        m, n = dp[i][j]
        if d + j > dp[i][j][0]:
            m += d
            if m > n: m, n = n, m
            dp[i + 1][j] = (m, n)
        else:
            dp[i + 1][d + j] = max(dp[i + 1][d + j][:], (m, n))
            ans = max(ans, d + j)

print(ans)
