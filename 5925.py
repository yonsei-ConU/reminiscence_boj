import sys
from collections import deque, defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = minput()
g = [input_().rstrip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [[[N * M] * M for _ in range(N)] for __ in range(3)]
cnt = 0

for sy in range(N):
    for sx in range(M):
        if g[sy][sx] == 'X' and not visited[sy][sx]:
            comp = [(sy, sx)]
            q = deque([(sy, sx)])
            visited[sy][sx] = True
            while q:
                cy, cx = q.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if not (0 <= nx < M and 0 <= ny < N) or visited[ny][nx]:
                        continue
                    if g[ny][nx] == 'X':
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        comp.append((ny, nx))
            q = deque(comp)
            for y, x in q:
                dist[cnt][y][x] = 0
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if not (0 <= nx < M and 0 <= ny < N and dist[cnt][ny][nx] == N * M):
                        continue
                    elif g[ny][nx] == '.':
                        q.append((ny, nx))
                        dist[cnt][ny][nx] = dist[cnt][y][x] + 1
                    else:
                        q.appendleft((ny, nx))
                        dist[cnt][ny][nx] = dist[cnt][y][x]
            cnt += 1

ans = N * M
for y in range(N):
    for x in range(M):
        tmp = dist[0][y][x] + dist[1][y][x] + dist[2][y][x]
        if g[y][x] == '.':
            tmp -= 2
        ans = min(ans, tmp)

print(ans)
