import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    if (not dp[i - 1]) or (i >= 3 and not dp[i - 3]) or (i >= 4 and not dp[i - 4]):
        dp[i] = 1

print("CSYK"[dp[N]::2])
