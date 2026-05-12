import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dijkstra(g, st):
    '''
    g: graph, g[start] = (end, dist)
    st: start node
    '''
    import heapq
    distances = [[float('inf'), float('inf')] for _ in range(len(g))]
    distances[st] = [0, 1]
    heap = []
    heapq.heappush(heap, (0, 1, st))

    while heap:
        dist, vertices, cur = heapq.heappop(heap)
        if distances[cur][0] < dist:
            continue
        for nextnum, nextdist in g[cur]:
            t = dist + nextdist
            if distances[nextnum][0] > t or (distances[nextnum][0] == t and distances[nextnum][1] > vertices + 1):
                distances[nextnum][0] = t
                distances[nextnum][1] = vertices + 1
                heapq.heappush(heap, (t, vertices + 1, nextnum))

    return distances


N, R = minput()
g = [[] for _ in range(N)]
for _ in range(R):
    a, b, c, d, e = minput()
    a -= 1; b -= 1
    cost = c + d * max(0, e - 10)
    g[a].append((b, cost))

distances = dijkstra(g, 0)
a, b = distances[-1]
if a == float('inf'):
    print('It is not a great way.')
else:
    print(a, b)
