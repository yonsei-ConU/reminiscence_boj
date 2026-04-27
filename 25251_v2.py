import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


h, w = minput()
house = [input_().rstrip() for _ in range(h)]
dp = [[float('inf')] * w for _ in range(h)]
for i in range(h):
    dp[i][-1] = +(house[i][-1] == 'C')
for j in range(w):
    dp[0][j] = +(house[0][j] == 'C')
for d in dp: print(*d)
for i in range(1, h):
    for j in range(w - 2, -1, -1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j + 1], dp[i - 1][j + 1] + 1) + (house[i][j] == 'C')

for d in dp: print(*d)
print(dp[-1][0])
