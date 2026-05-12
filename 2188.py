import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.reverse = None

    def __repr__(self):
        return f"({self.end}, {self.capacity})"


def add_edge(g, start, end, capacity):
    forward = Edge(start, end, capacity)
    backward = Edge(end, start, 0)
    forward.reverse = backward
    backward.reverse = forward
    g[start].append(forward)
    g[end].append(backward)


def edmond_karp(g, source, sink):
    """
    Edge class MUST be used
    Edge.reverse MUST be precalculated
    """
    from collections import deque
    N = len(g)
    ret = 0

    while 1:
        parent = [None] * N
        parent[source] = Edge(-1, -1, 0)
        q = deque([source])
        while q and parent[sink] is None:
            cur = q.popleft()
            for next_edge in g[cur]:
                nxt = next_edge.end
                if next_edge.capacity > next_edge.flow and parent[nxt] is None:
                    q.append(nxt)
                    parent[nxt] = next_edge

        if parent[sink] is None:
            break

        amount = 1000000
        cur = sink
        while cur != source:
            edge = parent[cur]
            amount = min(amount, edge.capacity - edge.flow)
            cur = edge.start

        ret += amount
        cur = sink
        while cur != source:
            edge = parent[cur]
            edge.flow += amount
            edge.reverse.flow -= amount
            cur = edge.start

    return ret


N, M = minput()
g = [[] for _ in range(N + M + 2)]
for i in range(1, N + 1):
    add_edge(g, 0, i, 1)
for i in range(1, N + 1):
    cnt, *cnrtk = minput()
    for c in cnrtk:
        add_edge(g, i, N + c, 1000000)
for i in range(N + 1, N + M + 1):
    add_edge(g, i, N + M + 1, 1)
ans = edmond_karp(g, 0, N + M + 1)
print(ans)
