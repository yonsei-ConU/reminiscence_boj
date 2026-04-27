import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
dp = [0] * (N + 1)
dp[2] = 1

for i in range(3, N + 1):
    next_state = set()
    for j in range(i - 1):
        next_state.add(dp[j] ^ dp[i - 2 - j])
    mex = 0
    while mex in next_state:
        mex += 1
    dp[i] = mex

print(2 - bool(dp[N]))
