import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def topological_sort(graph, indegree):
    zero_indegree = deque([node for node in range(N) if indegree[node] == 0])
    free = [True] * (len(indegree) + 1)

    result = [0] * N
    current_fastest_time = S[:]
    while zero_indegree:
        node = zero_indegree.popleft()
        result[node] = current_fastest_time[node]
        free[node] = False
        for neighbor, dist in graph[node]:
            indegree[neighbor] -= 1
            current_fastest_time[neighbor] = max(current_fastest_time[neighbor], result[node] + dist)
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    for i in range(N):
        if free[i]:
            result[i] = current_fastest_time[i]

    return result


N, M, C = minput()
S = list(minput())
memory = [[] for _ in range(N)]
indegree = [0] * N
for _ in range(C):
    a, b, x = minput()
    memory[a - 1].append((b - 1, x))
    indegree[b - 1] += 1

res = topological_sort(memory, indegree)
for r in res:
    print(r)
