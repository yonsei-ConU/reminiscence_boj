import sys
from collections import defaultdict
import heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st, end):
    '''
    g: graph, g[start] = (end, dist)
    st: start node
    '''
    distances = defaultdict(lambda: float('inf'))
    distances[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))

    while heap:
        dist, cur = heapq.heappop(heap)
        if cur == end:
            return distances[end]
        if distances[cur] < dist:
            continue
        for nextnum, nextdist in g[cur]:
            t = dist + nextdist
            if distances[nextnum] > t:
                distances[nextnum] = t
                heapq.heappush(heap, (t, nextnum))


N = int(input_())
A = list(minput())

exist = [False] * N
for i in range(N):exist[A[i] - 1] = True
exist = [i for i in range(N) if exist[i]]
new_A = []
