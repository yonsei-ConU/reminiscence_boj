import sys
for n in sys.stdin:
    n = int(n)
    dp = [1, 1, 3]
    for i in range(3, n + 1):
        dp.append(dp[-1] + 2 * dp[-2])

    print(dp[n])
