import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


enfnakfl = input_().rstrip()
ehfekfl = [input_().rstrip() for _ in range(2)]
# dp[i][j] = (enfnakfl i-th, ehfekfl j-th)
dp = [[0] * len(ehfekfl[0]) * 2 for _ in range(len(enfnakfl))]
for i in range(len(ehfekfl[0])):
    if ehfekfl[0][i] == enfnakfl[0]:
        dp[0][2 * i] = 1
    if ehfekfl[1][i] == enfnakfl[0]:
        dp[0][2 * i + 1] = 1

for i in range(1, len(enfnakfl)):
    for j in range(len(ehfekfl[0]) * 2):
        if ehfekfl[j % 2][j // 2] == enfnakfl[i]:
            dp[i][j] += sum(dp[i - 1][x] for x in range((j + 1) % 2, j - j % 2, 2) if ehfekfl[(j + 1) % 2][x // 2] == enfnakfl[i - 1])

print(sum(dp[-1]))
# 1:17:15