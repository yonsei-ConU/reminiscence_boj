import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    prime_check = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if prime_check[i]:
            for j in range(i * i, n + 1, i):
                prime_check[j] = False
    return prime_check


def dijkstra(g, st):
    '''
    g: graph, g[start] = (end, dist)
    st: start node
    '''
    import heapq
    distances = [float('inf')] * len(g)
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
                heapq.heappush(heap, (t, nextnum))

    return distances


N, M = minput()
p = sieve(10000000)
D = list(minput())
g = [defaultdict(lambda : 2147483647) for _ in range(N)]
for _ in range(M):
    u, v, w = minput()
    u -= 1; v -= 1
    if p[D[u] + D[v]]:
        g[u][v] = min(g[u][v], w)
        g[v][u] = min(g[v][u], w)

ans = dijkstra(g, 0)[-1]
if ans != float('inf'):
    print(ans)
else:
    print("Now where are you?")
