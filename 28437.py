import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())

dp = [0] * 100001
for a in A: dp[a] = 1

for i in range(1, 100001):
    for j in range(2 * i, 100001, i):
        dp[j] += dp[i]


Q = int(input_())
L = list(minput())
print(*[dp[i] for i in L])
