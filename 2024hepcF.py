import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from collections import deque

N = int(input_())
M = int(input_())
g = [[-1] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    u, v, d = minput()
    if u != v:
        g[u][v] = max(g[u][v], d)

ans = -1
q = deque([(0, 0, 0)])  # current vertex, time, visited vertex
while q:
    cur, time, visited = q.popleft()
    for i in range(N + 1):
        if g[cur][i] != -1 and not visited & (1 << i):
            if i == 0 and visited == (1 << (N + 1)) - 2:
                ans = max(time + g[cur][i], ans)
            else:
                q.append((i, time + g[cur][i], visited | (1 << i)))

print(ans)
