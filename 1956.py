import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def floyd_warshall(g):
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][k] + g[k][j], g[i][j])


V, E = minput()
g = [[999999999] * V for _ in range(V)]
for _ in range(E):
    a, b, c = minput()
    g[a - 1][b - 1] = c

floyd_warshall(g)
ans = 999999999
for i in range(V):
    ans = min(ans, g[i][i])

print(ans if ans < 999999999 else -1)
