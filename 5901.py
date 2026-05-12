import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    import heapq
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


N, M, K = minput()
markets = [int(input_()) - 1 for _ in range(K)]
g = [[] for _ in range(N)]
g2 = [{} for _ in range(N)]

for _ in range(M):
    i, j, L = minput()
    i -= 1; j -= 1
    g[i].append((j, L))
    g[j].append((i, L))
    g2[i][j] = L
    g2[j][i] = L

dist = [[] for _ in range(N)]
for i in range(K):
    market = markets[i]
    dist[market] = dijkstra(g, market)

ans = 10 ** 12
for home in range(N):
    if home in markets:
        continue
    for P in permutations(markets):
        p = list(P) + [home]
        if p[0] in g2[home]:
            temp = g2[home][p[0]]
        else:
            continue
        for i in range(K):
            temp += dist[p[i]][p[i + 1]]
        ans = min(ans, temp)

print(ans)
