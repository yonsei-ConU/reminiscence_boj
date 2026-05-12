import sys
from algorithms import dijkstra
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10 ** 9 + 9
N, M, x, y = minput()
x -= 1; y -= 1
g = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = minput()
    u -= 1; v -= 1
    g[u].append((v, w))

dist = dijkstra(g, x)
t = dist[y]
if t == float('inf'):
    exit(print(-1))

q = deque([x])
dist2 = [-1] * N
dist2[x] = 0
while q:
    cur = q.popleft()
    for nxt, d in g[cur]:
        if dist2[nxt] == -1 and dist[cur] + d == dist[nxt]:
            dist2[nxt] = dist2[cur] + 1
            q.append(nxt)

dp = [0] * N
visited = [False] * N
dp[x] = 1
visited[x] = True
q = deque([x])
while q:
    cur = q.popleft()
    for nxt, d in g[cur]:
        if dist[cur] + d == dist[nxt] and dist2[cur] + 1 == dist2[nxt]:
            dp[nxt] = (dp[cur] + dp[nxt]) % MOD
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

print(dist[y])
print(dist2[y])
print(dp[y])