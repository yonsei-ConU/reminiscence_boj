import sys, heapq
from collections import defaultdict
from math import sqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


# walk 0.006, subway 0.0015
def add_edge(x1, y1, x2, y2, t):
    d = sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2)) * t
    g[(x1, y1)].append(((x2, y2), d))
    g[(x2, y2)].append(((x1, y1), d))


def dijkstra(g, st):
    distances = {}
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if distances[cur] < dist:
            continue
        for nextnum, nextdist in g[cur]:
            t = dist + nextdist
            if distances.get(nextnum, float('inf')) > t:
                distances[nextnum] = t
                heapq.heappush(heap, (t, nextnum))

    return distances


c = 0
g = defaultdict(list)
subway = []
for line in sys.stdin:
    if not c:
        hx, hy, sx, sy = map(int, line.split())
        add_edge(hx, hy, sx, sy, 0.006)
        c = 1
    else:
        l = list(map(int, line.split()))
        stations = []
        for i in range(0, len(l) - 2, 2):
            stations.append((l[i], l[i + 1]))
            add_edge(hx, hy, l[i], l[i + 1], 0.006)
            add_edge(sx, sy, l[i], l[i + 1], 0.006)
        subway.append(stations)

for i in range(len(subway)):
    for j in range(len(subway[i]) - 1):
        add_edge(subway[i][j][0], subway[i][j][1], subway[i][j + 1][0], subway[i][j + 1][1], 0.0015)
    for j in range(i):
        for x1, y1 in subway[i]:
            for x2, y2 in subway[j]:
                add_edge(x1, y1, x2, y2, 0.006)

ans = dijkstra(g, (hx, hy))
print(round(ans[(sx,sy)]))
