import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
dp = [0, 0, 0, 0, 1, 2]
for i in range(6, n + 1):
    if not i % 2:
        dp.append(2 + dp[i >> 1])
    else:
        dp.append(2 + dp[(i >> 1) + 1])

print(dp)
