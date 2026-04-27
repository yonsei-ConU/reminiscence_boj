import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def a(x): print(*x, sep='\n')


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
m, n = minput()
g = [list(map(int, list(input_().rstrip()))) for _ in range(m)]
new_g = [[0] * n for _ in range(m)]
ans = 0

while True:
    cc = 0
    new_g = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if g[i][j] and not visited[i][j]:
                new_g[i][j] = max(g[i][j], new_g[i][j])
                q_ = deque()
                q_.append((i, j))
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                cc += 1
                # find current component
                while q_:
                    y, x = q_.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if not (0 <= ny < m and 0 <= nx < n) or visited[ny][nx] or g[ny][nx] != g[y][x]:
                            continue
                        q.append((ny, nx))
                        q_.append((ny, nx))
                        visited[ny][nx] = True
                        new_g[ny][nx] = max(g[ny][nx], new_g[ny][nx])
                a(new_g)
                print()
                # find cells with dist <= g[i][j]
                max_dist = g[i][j]
                dist = [[1000] * n for _ in range(m)]
                for y, x in q: dist[y][x] = 0
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if not (0 <= ny < m and 0 <= nx < n) or dist[ny][nx] != 1000:
                            continue
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        dist[ny][nx] = dist[y][x] + 1
                for y in range(m):
                    for x in range(n):
                        if dist[y][x] <= max_dist:
                            new_g[y][x] = max(new_g[y][x], g[i][j])
                a(new_g)
                print()
    if cc == 1:
        break
    ans += 1
    g, new_g = new_g, g

print(ans)
