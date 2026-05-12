import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    import heapq
    distances = [float('inf')] * (len(g) + 1)
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


T, C, Ts, Te = minput()
g = [[] for _ in range(T)]
for _ in range(C):
    R1, R2, c = minput()
    R1 -= 1; R2 -= 1
    g[R1].append((R2, c))
    g[R2].append((R1, c))

print(dijkstra(g, Ts - 1)[Te - 1])
