import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
seq = [list(minput())[2] for _ in range(N)]
if N == 1: exit(print(seq[0]))
if N == 2: exit(print(max(seq)))
dp = [0] * N
dp[0] = seq[0]
dp[1] = seq[1]
dp[2] = max(dp[1], dp[0] + seq[2])
for i in range(3, N): dp[i] = max(dp[i - 1], dp[i - 2] + seq[i], dp[i - 3] + seq[i])
print(max(dp[-1], dp[-2]))
