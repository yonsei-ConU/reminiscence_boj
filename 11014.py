import sys
from algorithms import add_edge, dinitz
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [-1, 0, 1]

for _ in range(int(input_())):
    N, M = minput()
    grid = []
    V = 0
    for i in range(N):
        s = input_().rstrip()
        V += s.count('.')
        grid.append(s)
    g = [[] for _ in range(N * M + 2)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'x':
                continue
            if j & 1:
                add_edge(g, i * M + j, N * M + 1, 1)
            else:
                add_edge(g, N * M, i * M + j, 1)
            for k in range(3):
                ny, nx = i + dy[k], j + 1
                if not (0 <= ny < N and 0 <= nx < M) or grid[ny][nx] != '.':
                    continue
                if j & 1:
                    add_edge(g, ny * M + nx, i * M + j, 1)
                else:
                    add_edge(g, i * M + j, ny * M + nx, 1)

    max_match = dinitz(g, N * M, N * M + 1)
    print(V - max_match)
