import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, k = minput()
c = sorted([int(input_()) for _ in range(n)])

dp = [200000] * 100001

for coin in c:
    dp[coin] = 1

for i in range(2, 100001):
    for coin in c:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != 200000 else -1)
