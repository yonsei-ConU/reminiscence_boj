import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
seq = list(minput())
dp = seq[:]
for i in range(1, N):
    dp[i] = max(dp[i - 1] + seq[i], dp[i])

print(max(dp))
