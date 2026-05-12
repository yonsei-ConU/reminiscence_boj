import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


s = input_().rstrip()
N = len(s)
dp = [-50000000] * N
if s[0] == '+':
    dp[0] = 10
    if s[1] == '-':
        dp[1] = 11
else:
    dp[0] = 1

for i in range(2, N):
    t = s[i - 1:i + 1]
    if t == '++':
        dp[i] = max(dp[i], dp[i - 2] + 10)
    elif t == '+-':
        dp[i] = max(dp[i], dp[i - 2] + 1)
    elif t == '-+':
        dp[i] = max(dp[i], dp[i - 2] - 10)
    else:
        dp[i] = max(dp[i], dp[i - 2] - 1)
    if i ^ 2:
        t = s[i - 2:i + 1]
        if t == '++-':
            dp[i] = max(dp[i], dp[i - 3] + 11)
        elif t == '-+-':
            dp[i] = max(dp[i], dp[i - 3] - 11)

print(dp[-1])
