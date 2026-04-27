import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                a[j] = False
    return tuple(primes)


primes = sieve(1120)
# dp[i][j] = (합이 i이고 쓰인 소수 개수가 j)
dp = [[0] * 15 for __ in range(1121)]
dp[0][0] = 1
for p in primes:
    for i in range(2, 1121)[::-1]:
        for j in range(1, 15)[::-1]:
            if i >= p:
                dp[i][j] += dp[i - p][j - 1]

for _ in range(int(input_())):
    n, k = minput()
    print(dp[n][k])
