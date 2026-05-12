import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def topological_sort(graph, indegree):
    zero_indegree = deque([i for i in range(N) if not indegree[i]])
    free = [True] * len(indegree)

    result = []
    while zero_indegree:
        node = zero_indegree.popleft()
        result.append(node)
        free[node] = False
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    assert len(result) == len(graph)

    return result + [i for i in range(len(free)) if i and free[i]]


N = int(input_())
raw = [list(minput()) for _ in range(N)]
prefer = [[] for _ in range(N)]

for i in range(N):
    j = i + 1
    k = 0
    while raw[i][k] != j:
        prefer[i].append(raw[i][k])
        k += 1
    prefer[i].append(j)

g = [[] for _ in range(N)]
indegree = [0] * N
s = [set(p) for p in prefer]
for i in range(N):
    for j in range(i):
        if s[i] < s[j]:
            g[i].append(j)
            indegree[j] += 1
        elif s[j] < s[i]:
            g[j].append(i)
            indegree[i] += 1

order = topological_sort(g, indegree)

ans = []
for i in range(N):
    ...
