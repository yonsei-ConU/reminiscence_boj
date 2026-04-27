import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    distances = [float('inf')] * len(g)
    distances[st] = 0
    second_dist = [float('inf')] * len(g)
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if second_dist[cur] < dist:
            continue
        for nextnum, nextdist in g[cur]:
            t = dist + nextdist
            if distances[nextnum] > t:
                second_dist[nextnum] = distances[nextnum]
                distances[nextnum] = t
                heapq.heappush(heap, (t, nextnum))
            elif second_dist[nextnum] > t:
                second_dist[nextnum] = t
                heapq.heappush(heap, (t, nextnum))

    return second_dist


N, R = minput()
g = [[] for _ in range(N)]

for _ in range(R):
   A, B, D = minput()
   A -= 1; B -= 1
   g[A].append((B, D))
   g[B].append((A, D))

print(dijkstra(g, 0)[-1])
