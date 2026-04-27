import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def bellman_ford(g, st):
    """
    g: graph, g[cur] = (nxt, dist)
    st: the vertex to start
    return: if there exists a negative cycle, False
            if there does not, distances list
    """
    v = len(g)
    distances = [float('inf')] * v
    distances[st] = 0

    for i in range(v - 1):
        for cur in range(v):
            for nxt, dist in g[cur]:
                if distances[cur] != float('inf') and distances[cur] + dist < distances[nxt]:
                    distances[nxt] = distances[cur] + dist

    for cur in range(v):
        for nxt, dist in g[cur]:
            if distances[cur] != float('inf') and distances[cur] + dist < distances[nxt]:
                return False

    return distances


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = minput()
    g[A - 1].append((B - 1, C))

distances = bellman_ford(g, 0)

if not distances:
    print(-1)
else:
    for d in distances[1:]:
        print(d if d != float('inf') else -1)
