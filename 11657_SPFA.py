import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def SPFA(g, st):
    """
    g: graph, g[cur] = (nxt, dist)
    st: the vertex to start
    return: if there exists a negative cycle, False
            if there does not, distances list
    """
    from collections import deque
    v = len(g)
    distances = [float('inf')] * v
    distances[st] = 0

    q = deque([st])
    in_queue = [False] * v
    in_queue[st] = True
    cnt = [0] * v
    cnt[st] = 1

    while q:
        cur = q.popleft()
        in_queue[cur] = False
        for nxt, dist in g[cur]:
            if distances[cur] + dist < distances[nxt]:
                distances[nxt] = distances[cur] + dist
                if not in_queue[nxt]:
                    in_queue[nxt] = True
                    q.append(nxt)
                    cnt[nxt] += 1
                    if cnt[nxt] >= v:
                        return False

    return distances


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = minput()
    g[A - 1].append((B - 1, C))

distances = SPFA(g, 0)

if not distances:
    print(-1)
else:
    for d in distances[1:]:
        print(d if d != float('inf') else -1)
