import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g, n):
    '''
    g: graph, g[start][end] = dist
    n: number of vertices
    return: distance matrix
    '''
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    g[i][j] = min(g[i][k] + g[k][j], g[i][j])
    return g


N, M = minput()
g = [[10 ** 10] * N for _ in range(N)]
for _ in range(M):
    A, B, C = minput()
    g[A - 1][B - 1] = C
    g[B - 1][A - 1] = C

dist = floyd_warshall(g, N)

min_idx = -1
min_val = 10 ** 18
for i in range(N):
    d = sum(dist[i])
    if d < min_val:
        min_idx = i
        min_val = d

print(min_idx + 1)
