import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
g = [[] for _ in range(N)]
P = list(minput())
for i in range(N - 1):
    g[i + 1].append(P[i] - 1)
    g[P[i] - 1].append(i + 1)

dist = [-1] * N
dist[0] = 0
q = deque([0])
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

depth = [0] * N
for d in dist:
    depth[d] += 1

ans = 0
for i in range(2, N + 1):
    ans = max(ans, sum(depth[::i]))

print(ans)
