import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g, n):
    '''
    g: graph
    g[start][end] = dist
    n: number of vertices
    return: distance matrix
    '''
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    g[i][j] = min(g[i][k] + g[k][j], g[i][j])
    return g


n, m, r = minput()
items = [0] + list(minput())
g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    g[i][i] = 0
for _ in range(r):
    a, b, l = minput()
    g[a][b] = l
    g[b][a] = l

dist = floyd_warshall(g, n)
ans = 0
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if dist[i][j] <= m:
            temp += items[j]
    ans = max(ans, temp)

print(ans)
