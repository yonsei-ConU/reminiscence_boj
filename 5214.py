import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K, M = minput()
g = [[] for _ in range(N + M)]

for i in range(M):
    hypertube = list(minput())
    for h in hypertube:
        g[N + i].append(h - 1)
        g[h - 1].append(N + i)

q = deque([0])
dist = [-2] * (N + M)
dist[0] = 2
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if dist[nxt] == -2:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(dist[N - 1] // 2)
