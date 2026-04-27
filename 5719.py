import sys, heapq
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    v = len(g)
    distances = [float('inf')] * v
    last = [[] for _ in range(v)]
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if distances[cur] < dist:
            continue
        for nextnum in g[cur]:
            nextdist = g[cur][nextnum]
            t = dist + nextdist
            if distances[nextnum] > t:
                distances[nextnum] = t
                last[nextnum] = [cur]
                heapq.heappush(heap, (t, nextnum))
            elif distances[nextnum] == t:
                last[nextnum].append(cur)

    return distances, last


while 1:
    N, M = minput()
    if not N:
        break
    g = [{} for _ in range(N)]
    S, D = minput()
    for _ in range(M):
        U, V, P = minput()
        g[U][V] = P
    _, last = dijkstra(g, S)
    q = deque([D])
    visited = [False] * N
    visited[D] = True
    while q:
        cur = q.popleft()
        for prev in last[cur]:
            if cur in g[prev]:
                del g[prev][cur]
                if not visited[prev]: q.append(prev)
    ans, _ = dijkstra(g, S)
    print(ans[D] if ans[D] != float('inf') else -1)
