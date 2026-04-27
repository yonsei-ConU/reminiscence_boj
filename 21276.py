import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def topological_sort(graph, indegree):
    zero_indegree = deque([node for node in graph if indegree[node] == 0])
    roots = list(zero_indegree)
    direct_child = {name: [] for name in names}
    free = {name: True for name in indegree}

    while zero_indegree:
        node = zero_indegree.popleft()
        free[node] = False
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)
                direct_child[node].append(neighbor)

    for name in free:
        if free[name]:
            roots.append(name)
    return roots, direct_child


N = int(input_())
names = sorted(input_().split())
g = {name: [] for name in names}
indegree = {name: 0 for name in names}

for _ in range(int(input_())):
    child, parent = input_().split()
    g[parent].append(child)
    indegree[child] += 1

roots, direct_child = topological_sort(g, indegree)
print(len(roots))
roots.sort()
print(' '.join(roots))

for name in names:
    dc = direct_child[name]
    print(name, len(dc), ' '.join(sorted(dc)))
