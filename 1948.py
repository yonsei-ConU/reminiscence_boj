import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def topological_sort(graph, indegree):
    zero_indegree = deque([i for i in range(len(graph)) if not indegree[i]])
    dist = [[-float('inf'), []]] * len(graph)
    for start in zero_indegree:
        dist[start] = [0, []]

    while zero_indegree:
        node = zero_indegree.popleft()
        for neighbor, weight in graph[node]:
            if dist[node][0] + weight > dist[neighbor][0]:
                dist[neighbor] = [dist[node][0] + weight, [node]]
            elif dist[node][0] + weight == dist[neighbor][0]:
                dist[neighbor][1].append(node)
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    return dist


n = int(input_())
m = int(input_())
g = [[] for _ in range(n)]
indegree = [0] * n
for _ in range(m):
    s, e, t = minput()
    g[s - 1].append((e - 1, t))
    indegree[e - 1] += 1

dist = topological_sort(g, indegree)
s, e = minput()
s -= 1
e -= 1
assert dist[s] == [0, []]
longest = dist[e][0]

paths = 0
trace = deque([e])
visited = [False] * n
visited[e] = True
while trace:
    cur = trace.popleft()
    paths += len(dist[cur][1])
    for nxt in dist[cur][1]:
        if not visited[nxt]:
            visited[nxt] = True
            trace.append(nxt)

print(longest)
print(paths)
