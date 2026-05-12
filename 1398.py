import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dp = [float('inf')] * 101
dp[0] = 0
for i in range(1, 101):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    if i >= 10:
        dp[i] = min(dp[i], dp[i - 10] + 1)
    if i >= 25:
        dp[i] = min(dp[i], dp[i - 25] + 1)

for _ in range(int(input_())):
    price = int(input_())
    ans = 0
    while price:
        ans += dp[price % 100]
        price //= 100
    print(ans)
