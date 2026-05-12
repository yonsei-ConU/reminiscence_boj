import sys
from algorithms import matrix_pow
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 1000003
N, S, E, T = minput()
mat = [input_().rstrip() for _ in range(N)]
g = [[] for _ in range(5 * N)]

for i in range(N):
    for j in range(N, 5 * N, N):
        g[i + j].append(i + j - N)

for i in range(N):
    for j in range(N):
        x = int(mat[i][j])
        if not x: continue
        else:
            g[i].append(N * (x - 1) + j)

adj = [[0] * 5 * N for _ in range(5 * N)]
for i in range(5 * N):
    for nxt in g[i]:
        adj[i][nxt] = 1

ans = matrix_pow(adj, T, MOD)
print(ans[S - 1][E - 1])
