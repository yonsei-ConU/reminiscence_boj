import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def greedy(n):
    ret = 0
    for coin in c:
        ret += n // coin
        n %= coin
    return ret


n = int(input_())
c = list(minput())[::-1]

dp = [200000] * 100001

for coin in c:
    dp[coin] = 1

for i in range(2, 100001):
    for coin in c:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

for i in range(1, 100001):
    if greedy(i) != dp[i]:
        print(i)
        break
else:
    print(-1)
