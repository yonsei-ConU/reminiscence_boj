import sys
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


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


N = int(input_())
M = int(input_())
chessboard = [[1] * N for _ in range(N)]

for _ in range(M):
    i, j = minput()
    chessboard[i][j] = 0

u = v = check = 0
diagonals = [[[] for _ in range(N)] for _ in range(N)]

for sum_ in range(2 * N - 1):
    u += check
    check = 0
    start = max(0, sum_ - (N - 1))
    end = start + min(sum_ + 1, 2 * N - 1 - sum_)
    for i in range(start, end):
        j = sum_ - i
        if chessboard[i][j]:
            diagonals[i][j].append(u)
            check = 1
        else:
            u += check
            check = 0

check = 0
for diff in range(-N + 1, N):
    v += check
    check = 0
    start = max(0, -diff)
    end = start + N - abs(diff)
    for i in range(start, end):
        j = i + diff
        assert 0 <= j < N
        if chessboard[i][j]:
            diagonals[i][j].append(v)
            check = 1
        else:
            v += check
            check = 0

adj = [[] for _ in range(u + 1)]
for i in range(N):
    for j in range(N):
        if diagonals[i][j]:
            p, q = diagonals[i][j]
            adj[p].append(q)

print(hopcroft_karp(adj, u + 1, v + 1))
