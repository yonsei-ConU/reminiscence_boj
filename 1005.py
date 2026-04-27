import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for p in range(int(input_())):
    N, K = minput()
    D = list(minput())
    graph = [[] for _ in range(N)]
    g_reverse = [[] for _ in range(N)]
    indegree = [0] * N
    for i in range(K):
        X, Y = minput()
        X -= 1
        Y -= 1
        graph[X].append(Y)
        g_reverse[Y].append(X)
        indegree[Y] += 1
    W = int(input_())

    zero_indegree = deque([node for node in range(len(indegree)) if indegree[node] == 0])
    dist = [float('inf')] * len(indegree)
    for zi in zero_indegree:
        dist[zi] = D[zi]

    while zero_indegree:
        node = zero_indegree.popleft()
        if g_reverse[node]:
            dist[node] = max(dist[x] for x in g_reverse[node]) + D[node]
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    print(dist[W - 1])
