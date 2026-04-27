import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g, n):
    trace = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] < 10 ** 18:
                trace[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif g[i][k] + g[k][j] < g[i][j]:
                    trace[i][j] = trace[k][j]
                    g[i][j] = g[i][k] + g[k][j]
                elif g[i][k] + g[k][j] == g[i][j]:
                    trace[i][j] = 998244353
    return g, trace


N, M = minput()
g = [[10 ** 18] * N for _ in range(N)]
edges = [{} for _ in range(N)]  # edges[i][j]: i에서 j로 가는 간선 번호

for idx in range(M):
    u, v, time = minput()
    g[u][v] = g[v][u] = time
    edges[u][v] = idx
    edges[v][u] = idx

ans = [0] * M
g, trace = floyd_warshall(g, N)

for i in range(N):
    for j in range(i):
        # i -> j
        path = [j]
        cur = j
        unique = True
        while cur != i:
            if trace[i][cur] == 998244353:
                unique = False
                break
            cur = trace[i][cur]
            path.append(cur)
        if unique:
            for k in range(len(path) - 1):
                ans[edges[path[k]][path[k + 1]]] += 1

print(*ans)
