import sys
from bisect import bisect_left as lower_bound, bisect_right as upper_bound
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10007
S = input_().rstrip()
N = len(S)
if N == 1: exit(print(1))
elif N == 2: exit(print(4 - len(set(S))))
# dp[i][j] = i ~ j번 인덱스 사이 팰린드롬 개수
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    dp[i][i + 1] = 2 + (S[i] == S[i + 1])

for diff in range(2, N):
    for start in range(N - diff):
        end = start + diff
        if S[start] == S[end]:
            dp[start][end] = (dp[start][end - 1] + dp[start + 1][end] + 1) % MOD
        else:
            dp[start][end] = (dp[start][end - 1] + dp[start + 1][end] - dp[start + 1][end - 1]) % MOD
print(dp[0][-1])
