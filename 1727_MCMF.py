import sys, heapq
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class MCMFEdge:
    def __init__(self, start, end, capacity, cost):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.cost = cost
        self.flow = 0
        self.reverse = None

    def __repr__(self):
        return f"({self.end}, cap: {self.capacity}, flow: {self.flow}, cost: {self.cost})"


def add_edge_mcmf(graph, start, end, capacity, cost):
    forward = MCMFEdge(start, end, capacity, cost)
    backward = MCMFEdge(end, start, 0, -cost)
    forward.reverse = backward
    backward.reverse = forward
    graph[start].append(forward)
    graph[end].append(backward)


def MCMF(graph, source, sink):
    INF = float('inf')
    n = len(graph)

    potential = [0] * n

    flow = 0
    min_cost = 0

    while True:
        dist = [INF] * n
        parent = [(-1, None)] * n
        dist[source] = 0

        visited_nodes = []

        pq = [(0, source)]
        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist != dist[u]:
                continue
            visited_nodes.append(u)
            for edge in graph[u]:
                if edge.flow < edge.capacity:
                    cost_u_v = edge.cost + potential[u] - potential[edge.end]
                    nd = cur_dist + cost_u_v
                    if nd < dist[edge.end]:
                        dist[edge.end] = nd
                        parent[edge.end] = (u, edge)
                        heapq.heappush(pq, (nd, edge.end))

        if dist[sink] == INF:
            break

        for u in visited_nodes:
            if dist[u] < INF:
                potential[u] += dist[u]

        increment_flow = INF
        v = sink
        while v != source:
            u, edge = parent[v]
            if u == -1:
                increment_flow = 0
                break
            increment_flow = min(increment_flow, edge.capacity - edge.flow)
            v = u

        if not increment_flow:
            break

        v = sink
        while v != source:
            u, edge = parent[v]
            edge.flow += increment_flow
            edge.reverse.flow -= increment_flow
            min_cost += edge.cost * increment_flow
            v = u

        flow += increment_flow

    return flow, min_cost


n, m = minput()
g = [[] for _ in range(n + m + 2)]
M = list(minput())
F = list(minput())
for i in range(n):
    add_edge_mcmf(g, 0, i + 1, 1, 0)
for i in range(n + 1, n + m + 1):
    add_edge_mcmf(g, i, n + m + 1, 1, 0)

for i in range(n):
    for j in range(m):
        add_edge_mcmf(g, i + 1, n + j + 1, 1, abs(M[i] - F[j]))

flow, ans = MCMF(g, 0, n + m + 1)
assert flow == min(n, m)
print(ans)
