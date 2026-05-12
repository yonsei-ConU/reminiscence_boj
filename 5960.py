import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 97654321
U, L, P = minput()
pairs = [input_().rstrip() for _ in range(P)]
# dp[i][j][k] = (i개의 대문자, j개의 소문자를 사용했으며 마지막 글자가 k인 경우의 수)
dp = [[[0] * (97 + 26) for _ in range(L + 1)] for __ in range(U + 1)]
g = [[] for _ in range(97 + 26)]
for pair in pairs:
    a, b = map(ord, pair)
    g[a].append(b)
    if a < 97:
        dp[1][0][a] = 1
    else:
        dp[0][1][a] = 1

r = list(range(65, 65 + 26)) + list(range(97, 97 + 26))
for i in range(U + 1):
    for j in range(L + 1):
        for k in r:
            for nxt in g[k]:
                if nxt < 97 and i != U:
                    dp[i + 1][j][nxt] = (dp[i + 1][j][nxt] + dp[i][j][k]) % MOD
                elif nxt >= 97 and j != L:
                    dp[i][j + 1][nxt] = (dp[i][j + 1][nxt] + dp[i][j][k]) % MOD

print(sum(dp[-1][-1]) % MOD)
