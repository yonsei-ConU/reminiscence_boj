import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dinitz(g, source, sink):
    N = len(g)
    level = [-1] * N
    ret = 0

    def dinitz_bfs():
        q = deque(source)
        level[source] = 0
        while q:
            cur = q.popleft()
            for edge in g[cur]:
                if level[edge.end] == -1 and edge.flow < edge.capacity:
                    q.append(edge.end)
                    level[edge.end] = level[cur] + 1
                    if edge.end == sink:
                        break
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
        d = dinitz_dfs(source, float('inf'))
        if not d:
            break
        ret += d

    return ret
