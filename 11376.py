import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def hopcroft_karp(adj, n, m):
    from collections import deque

    g_match = [-1] * n
    h_match = [-1] * m
    dist = [0] * n
    inf = float('inf')

    def hk_bfs():
        q = deque()
        for u in range(n):
            if g_match[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf

        ret = inf
        while q:
            u = q.popleft()
            if dist[u] >= ret:
                continue
            for v in adj[u]:
                if h_match[v] == -1:
                    ret = dist[u] + 1
                elif dist[h_match[v]] == inf:
                    dist[h_match[v]] = dist[u] + 1
                    q.append(h_match[v])

        return ret != inf

    def hk_dfs(u):
        for v in adj[u]:
            if h_match[v] == -1 or (dist[h_match[v]] == dist[u] + 1 and hk_dfs(h_match[v])):
                g_match[u] = v
                h_match[v] = u
                return True
        dist[u] = inf
        return False

    ret = 0
    while hk_bfs():
        for u in range(n):
            if g_match[u] == -1:
                ret += hk_dfs(u)

    return ret


N, M = minput()
adj = [[] for _ in range(2 * N)]

for i in range(N):
    cnt, *works = minput()
    for work in works:
        adj[i].append(work - 1)
        adj[i + N].append(work - 1)

print(hopcroft_karp(adj, 2 * N, M))
