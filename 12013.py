import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
seq = [int(input_()) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = seq[i]

for diff in range(1, N):
    for start in range(N):
        end = start + diff
        if end >= N:
            break
        for mid in range(start, end):
            if dp[start][mid] == dp[mid + 1][end] != 0:
                dp[start][end] = dp[start][mid] + 1

ans = 0
for d in dp:
    ans = max(ans, max(d))
print(ans)
