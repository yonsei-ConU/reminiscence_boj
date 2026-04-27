import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def asdf(y, x):
    if dp[y][x] or processed[y][x]:
        return dp[y][x]
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and heights[y][x] < heights[y + dy[i]][x + dx[i]]:
            dp[y][x] += asdf(y + dy[i], x + dx[i])
    processed[y][x] = True
    return dp[y][x]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, M = minput()
heights = [list(minput()) for _ in range(N)]
processed = [[False] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
asdf(N - 1, M - 1)
print(dp[-1][-1])
