import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, M = minput()
# g[i][j] = (연결된점, 가중치)
g = [[{} for __ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    s = input_()
    for j in range(M):
        if s[j] == '/':
            g[i][j][(i + 1, j + 1)] = 1
            g[i + 1][j + 1][(i, j)] = 1
            g[i + 1][j][(i, j + 1)] = 0
            g[i][j + 1][(i + 1, j)] = 0
        else:
            g[i][j][(i + 1, j + 1)] = 0
            g[i + 1][j + 1][(i, j)] = 0
            g[i + 1][j][(i, j + 1)] = 1
            g[i][j + 1][(i + 1, j)] = 1

q = deque([(0, 0)])
dist = [[987654321] * (M + 1) for _ in range(N + 1)]
dist[0][0] = 0

while q:
    y, x = q.popleft()
    for ny, nx in g[y][x]:
        if not (0 <= ny <= N and 0 <= nx <= M) or dist[ny][nx] <= dist[y][x] + g[y][x][(ny, nx)]:
            continue
        else:
            dist[ny][nx] = dist[y][x] + g[y][x][(ny, nx)]
            if g[y][x][(ny, nx)]:
                q.append((ny, nx))
            else:
                q.appendleft((ny, nx))

# \\\/\/
# /\\\\\
# //\///
# ////\\
# [[ 0, -1,  0, -1,  0, -1,  0],
#  [-1,  0, -1,  0, -1,  0, -1],
#  [ 0, -1,  0, -1,  0, -1,  0],
#  [-1,  0, -1,  0, -1,  0, -1],
#  [ 0, -1,  0, -1, -1, -1,  0]]
#
# [[ 0, -1,  1, -1,  1, -1,  1],
#  [-1,  0, -1,  1, -1,  1, -1],
#  [ 0, -1,  0, -1,  0, -1,  1],
#  [-1,  0, -1,  0, -1,  1, -1],
#  [ 0, -1,  0, -1,  1, -1,  1]]

print(dist[N][M] if dist[N][M] != 987654321 else 'NO SOLUTION')
