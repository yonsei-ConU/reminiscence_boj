import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1,-1,0,0]
dx = [0,0,1,-1]

N, M = minput()
g = []
for i in range(N):
    s = input_().rstrip()
    if (j := s.find('S')) != -1:
        q1 = [(i, j)]
    if (j := s.find('H')) != -1:
        q2 = [(i, j)]
    g.append(s)

q1 = deque(q1)
dist1 = [[10 ** 8] * M for _ in range(N)]
i, j = q1[0]
dist1[i][j] = 0
while q1:
    y, x = q1.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and g[ny][nx] != 'D' and dist1[ny][nx] == 10 ** 8:
            q1.append((ny, nx))
            dist1[ny][nx] = dist1[y][x] + 1

q2 = deque(q2)
dist2 = [[10 ** 8] * M for _ in range(N)]
i, j = q2[0]
dist2[i][j] = 0
while q2:
    y, x = q2.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and g[ny][nx] != 'D' and dist2[ny][nx] == 10 ** 8:
            q2.append((ny, nx))
            dist2[ny][nx] = dist2[y][x] + 1

ans = 10 ** 8
for i in range(N):
    for j in range(M):
        if g[i][j] == 'F':
            ans = min(ans, dist1[i][j] + dist2[i][j])

print(ans if ans != 10 ** 8 else -1)
