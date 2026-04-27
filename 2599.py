import sys
from collections import deque
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

        amount = float('inf')
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


N = int(input_())
INF = float('inf')
l = [list(minput()) for _ in '   ']
g = [[] for _ in range(8)]
for i in range(1, 4):
    add_edge(g, 0, i, l[i - 1][0])
add_edge(g, 1, 5, INF)
add_edge(g, 1, 6, INF)
add_edge(g, 2, 4, INF)
add_edge(g, 2, 6, INF)
add_edge(g, 3, 4, INF)
add_edge(g, 3, 5, INF)
for i in range(4, 7):
    add_edge(g, i, 7, l[i - 4][1])

ans = edmond_karp(g, 0, 7)
if ans != N:
    print(0)
else:
    print(1)
    print(g[1][1].flow, g[1][2].flow)
    print(g[2][1].flow, g[2][2].flow)
    print(g[3][1].flow, g[3][2].flow)
