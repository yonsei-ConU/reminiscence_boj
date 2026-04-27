import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def line_segment_intersection(a, b, c, d):
    def ccw(a, b, c):
        cross_product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if cross_product > 0:
            return 1
        elif cross_product < 0:
            return -1
        else:
            return 0

    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if ab == 0 and cd == 0:
        a, b = sorted([a, b])
        c, d = sorted([c, d])
        return not (b < c or d < a)

    return ab <= 0 and cd <= 0


class FlowEdge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.reverse = None

    def __repr__(self):
        return f"({self.end}, capacity: {self.capacity}, flow: {self.flow})"


def add_edge(g, start, end, capacity):
    forward = FlowEdge(start, end, capacity)
    backward = FlowEdge(end, start, 0)
    forward.reverse = backward
    backward.reverse = forward
    g[start].append(forward)
    g[end].append(backward)


def dinitz(g, source, sink):
    N = len(g)
    level = [-1] * N
    ret = 0

    def dinitz_bfs():
        nonlocal level
        level = [-1] * N
        q = deque([source])
        level[source] = 0
        while q:
            cur = q.popleft()
            for edge in g[cur]:
                if level[edge.end] == -1 and edge.flow < edge.capacity:
                    level[edge.end] = level[cur] + 1
                    q.append(edge.end)
        return level[sink] != -1

    def dinitz_dfs(cur, flow):
        if cur == sink:
            return flow
        while ptr[cur] < len(g[cur]):
            edge = g[cur][ptr[cur]]
            if level[edge.end] == level[cur] + 1 and edge.flow < edge.capacity:
                pushed = dinitz_dfs(edge.end, min(flow, edge.capacity - edge.flow))
                if pushed > 0:
                    edge.flow += pushed
                    edge.reverse.flow -= pushed
                    return pushed
            ptr[cur] += 1
        return 0

    while dinitz_bfs():
        ptr = [0] * N
        while True:
            pushed = dinitz_dfs(source, float('inf'))
            if pushed == 0:
                break
            ret += pushed

    return ret


N = int(input_())
hori = []
vert = []

for _ in range(N):
    obstacle = tuple(minput())
    if obstacle[0] == obstacle[2]:
        vert.append(obstacle)
    else:
        hori.append(obstacle)

h = len(hori)
v = len(vert)
# 0 source, 1 ~ h hori, h + 1 ~ N vert, N + 1 sink
g = [[] for _ in range(2 + N)]

for i in range(1, h + 1):
    add_edge(g, 0, i, 1)
for i in range(h + 1, N + 1):
    add_edge(g, i, N + 1, 1)
for i in range(1, h + 1):
    obs = hori[i - 1]
    for j in range(v):
        if line_segment_intersection((obs[0], obs[1]), (obs[2], obs[3]), (vert[j][0], vert[j][1]), (vert[j][2], vert[j][3])):
            add_edge(g, i, 1 + h + j, 1)

print(N - dinitz(g, 0, N + 1))
