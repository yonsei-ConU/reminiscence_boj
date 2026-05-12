import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def topological_sort(graph, indegree):
    zero_indegree = deque([i for i in range(len(graph)) if not indegree[i]])
    free = [True] * len(indegree)
    unfix = False
    result = []
    while zero_indegree:
        node = zero_indegree.popleft()
        if zero_indegree:
            unfix = True
        result.append(node)
        free[node] = False
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    assert len(result) == len(graph)

    return result + [i for i in range(len(free)) if i and free[i]], unfix


n = int(input_())
m = int(input_())
g = [[] for _ in range(n)]
indegree = [0] * n
for _ in range(m):
    a, b = minput()
    g[a - 1].append(b - 1)
    indegree[b - 1] += 1

order, unfix = topological_sort(g, indegree)
for o in order:
    print(o + 1)
if unfix:
    print(1)
else:
    print(0)
