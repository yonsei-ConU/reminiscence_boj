import sys
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) if int(x) else INF, input_().split())


INF = 23456789
N = int(input_())
costs = [list(minput()) for _ in range(N)]
ans = INF
# dp[i][mask] = 마지막으로 방문한 도시가 i이며 현재까지 방문한 도시 집합이 mask일 때 최소 시간
"""
mask는 항상 증가하는 방향으로만 상태전이됨
-> mask가 0부터 0b11111까지 돌면 됨
"""

for start in range(N):
    dp = [[INF] * (1 << N) for _ in range(N)]
    dp[start][1 << start] = 0

    for mask in range(1, 1 << N):
        for i in range(N):
            # i번 도시에서 다음 도시 nxt로 이동
            for nxt in range(N):
                if mask & (1 << nxt) or i == nxt:
                    continue
                dp[nxt][mask | (1 << nxt)] = min(dp[nxt][mask | (1 << nxt)], costs[i][nxt] + dp[i][mask])

    ans = min(ans, min(dp[x][-1] + costs[x][start] for x in range(N) if x != start))

print(ans)
