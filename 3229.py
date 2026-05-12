import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    distances = [float('inf')] * len(g)
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        time, cur = heapq.heappop(heap)
        if distances[cur] < time:
            continue
        for nxt in g[cur]:
            p1, p2 = min(cur, nxt), max(cur, nxt)
            if cur == p1:
                if not time % (2 * (p2 - p1)):
                    nexttime = time + p2 - p1
                else:
                    nexttime = time - time % (2 * (p2 - p1)) + 3 * (p2 - p1)
            else:
                if time % (2 * (p2 - p1)) and not time % (p2 - p1):
                    nexttime = time + p2 - p1
                elif time % (2 * (p2 - p1)) < p2 - p1:
                    nexttime = time + (p2 - p1 - time % (2 * (p2 - p1))) + p2 - p1
                else:
                    nexttime = time + p2 - p1 + 2 * (p2 - p1) - time % (2 * (p2 - p1)) + p2 - p1
            if distances[nxt] > nexttime:
                distances[nxt] = nexttime
                heapq.heappush(heap, (nexttime, nxt))

    return distances


K, N = minput()
g = [[] for _ in range(K)]
for _ in range(N):
    A, B = minput()
    A -= 1; B -= 1
    g[A].append(B)
    g[B].append(A)

distances = dijkstra(g, 0)
print(distances[-1] * 5)
