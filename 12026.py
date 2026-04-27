import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
block = input_().strip()
dp = [10 ** 18] * N
dp[0] = 0
for i in range(1, N):
    for j in range(i):
        if (block[j] == 'B' and block[i] == 'O') or (block[j] == 'O' and block[i] == 'J') or (block[j] == 'J' and block[i] == 'B'):
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

print(dp[-1] if dp[-1] < 10 ** 18 else -1)
