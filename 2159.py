import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
N = int(input_())
start = list(minput())
people = [list(minput()) for _ in range(N)]
# dp[i][j]: i번째 사람까지, 위치가 dydx[j]
dp = [[10 ** 18] * 5 for _ in range(N)]
for j in range(5):
    dp[0][j] = dist(start[0], start[1], people[0][0] + dx[j], people[0][1] + dy[j])

for i in range(1, N):
    # pj -> cj
    for pj in range(5):
        for cj in range(5):
            dp[i][cj] = min(dp[i][cj], dp[i - 1][pj] + dist(people[i - 1][0] + dx[pj], people[i - 1][1] + dy[pj], people[i][0] + dx[cj], people[i][1] + dy[cj]))

print(min(dp[-1]))
