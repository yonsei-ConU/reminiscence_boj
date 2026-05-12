import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 1000000
N = int(input_())
V = sorted([int(input_()) for _ in range(N)])
if N == 1:
    print(V[0])
    print(1)
    exit()

s = sum(V)
W = s >> 1
# dp[i][j] = i번째 동전까지만, 가치 합이 j가 되는 경우의 수
dp = [[0] * (W + 1) for _ in range(N)]
dp[0][0] = 1
dp[0][V[0]] = 1
for i in range(1, N):
    v = V[i]
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= v:
            dp[i][j] += dp[i - 1][j - v]
        dp[i][j] %= MOD

ans_diff = 999999999999
ans_dp = 0
for i in range(W + 1):
    if not dp[-1][i]:
        continue
    diff = abs(i - (s - i))
    if diff < ans_diff:
        ans_diff = diff
        ans_dp = dp[-1][i] % MOD
    elif diff == ans_diff:
        ans_dp = (ans_dp + dp[-1][i]) % MOD

print(ans_diff)
print(ans_dp)
