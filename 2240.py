import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


T, W = minput()
tree = []
streak = 0
last = -1
first = 0
for _ in range(T):
    x = int(input_())
    if x != last:
        if last != -1:
            if last == 1: tree.append([streak, 0])
            else: tree.append([0, streak])
        streak = 1
        last = x
    else:
        streak += 1
    if not first: first = x

if last == 1: tree.append([streak, 0])
else: tree.append([0, streak])
# dp[i][j][k]: until ith, j times changed, last tree k
dp = [[[-10000, -10000] for __ in range(W + 1)] for _ in range(len(tree))]
dp[0][0][0] = tree[0][0]
dp[0][1][1] = tree[0][1]
for i in range(1, len(tree)):
    for j in range(W + 1):
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + tree[i][0] if j else -10000, dp[i-1][j][0] + tree[i][0], dp[i-1][j-1][0] if j else -10000)
        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] + tree[i][1] if j else -10000, dp[i-1][j][1] + tree[i][1], dp[i-1][j-1][1] if j else -10000)
# print(tree)
# print(*dp, sep='\n')
res = dp[-1]
ans = -10000
for r in res:
    ans = max(ans, max(r))

print(ans)
