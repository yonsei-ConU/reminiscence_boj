import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n, m = minput()
q = deque()
g = []
dist = [[[-1, -1, -1, -1] for _ in range(m)] for __ in range(n)]
for y in range(n):
    s = input_().rstrip()
    S = s.find('S')
    E = s.find('E')
    if S != -1:
        for k in range(4):
            q.append((y, S, k))
            dist[y][S][k] = 0
    if E != -1:
        goal = ((y, E))
    g.append(s)

while q:
    y, x, d = q.popleft()
    for i in range(4):
        if i - d == 1 or i - d == -3:
            continue
        ny, nx = y + dy[i], x + dx[i]
        if not (0 <= ny < n and 0 <= nx < m) or dist[ny][nx][i] != -1 or g[ny][nx] == '#':
            continue
        q.append((ny, nx, i))
        dist[ny][nx][i] = dist[y][x][d] + 1

gy, gx = goal
ans = 10 ** 18
for val in dist[gy][gx]:
    if val != -1:
        ans = min(ans, val)

print(ans if ans != 10 ** 18 else -1)
