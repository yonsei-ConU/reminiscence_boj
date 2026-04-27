import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
N, M = minput()
X, Y = minput()
X -= 1; Y -= 1
dist = [[-1] * N for _ in range(N)]
dist[X][Y] = 0
q = deque()
q.append((X, Y))

while q:
    x, y = q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

for _ in range(M):
    A, B = minput()
    print(dist[A - 1][B - 1], end=' ')
