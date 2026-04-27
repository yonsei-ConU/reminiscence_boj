import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


sz = int(input_())
l, r = minput()
if l > r: l, r = r, l
q = int(input_())
A = [int(input_()) for _ in range(q)]
dp = [[10000000] * (q + 1) for _ in range(q + 1)]
dp[0][0] = 0
for i in range(q):
    for j in range(q):
        nxt = max(i, j) + 1
        dp[nxt][j] = min(dp[nxt][j], dp[i][j] + abs((A[i - 1] if i else l) - A[nxt - 1]))
        dp[i][nxt] = min(dp[i][nxt], dp[i][j] + abs((A[j - 1] if j else r) - A[nxt - 1]))

ans = 10000000
for i in range(q):
    ans = min(ans, dp[i][q], dp[q][i])
print(ans)
