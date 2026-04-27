import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def topological_sort(graph, indegree):
    from heapq import heapify, heappush, heappop
    zero_indegree = [node for node in graph if indegree[node] == 0]
    visited_cnt = 0
    visited = {node: False for node in graph}
    zero_indegree.sort(reverse=True)
    nxt = []
    result = []
    while 1:
        while zero_indegree:
            node = zero_indegree.pop()
            visited_cnt += 1
            visited[node] = True
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    nxt.append(neighbor)
        if not nxt:
            break
        zero_indegree = sorted(nxt, reverse=True)
        nxt = []

    if len(result) != len(graph):
        return ['-1']
    else:
        return result


N = int(input_())
graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(N):
    A, B = input_().split()
    graph[A].append(B)
    indegree[B] += 1

result = topological_sort(graph, indegree)
print('\n'.join(result))
