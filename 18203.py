import sys
import heapq
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    distances = [float('inf')] * len(g)
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if distances[cur] < dist:
            continue
        for nextnum, nextdist in g[cur]:
            t = dist + nextdist
            if distances[nextnum] > t:
                distances[nextnum] = t
                heapq.heappush(heap, (t, nextnum))

    return distances


n, m = minput()
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = minput()
    a -= 1; b -= 1
    g[a].append((b, t))
    g[b].append((a, t))

dragonball = set(map(lambda x: int(x) - 1, input_().split()))
if 0 in dragonball:
    dragonball.remove(0)
dragonball = list(dragonball)
dist = [[] for _ in range(n)]
for loc in dragonball + [0]:
    dist[loc] = dijkstra(g, loc)

ans = float('inf')
for p in permutations(dragonball):
    cur = 0
    tmp = 0
    valid = True

    for nxt in p:
        if dist[cur][nxt] == float('inf'):
            valid = False
            break
        tmp += dist[cur][nxt]
        cur = nxt

    if valid:
        ans = min(tmp, ans)

print(ans if ans != float('inf') else -1)
# 50:54