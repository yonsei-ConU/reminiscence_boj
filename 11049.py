import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N == 1: exit(print(0))
mat = list(minput())
for i in range(N - 1): mat.append(list(minput())[1])
dp = [[0] * N for _ in range(N)]

for delta in range(2, N + 1):
    start = 0
    while start + delta < N + 1:
        end = start + delta - 1
        dp[start][end] = min(dp[start][k] + dp[k + 1][end] + mat[start] * mat[k + 1] * mat[end + 1] for k in range(start, end))
        start += 1

print(dp[0][N-1])
