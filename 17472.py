import sys
from algorithms import UnionFind, kruskal
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = minput()
original_grid = [list(minput()) for _ in range(N)]
grid = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
comp = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] or not original_grid[i][j]:
            continue
        visited[i][j] = True
        grid[i][j] = comp
        comp += 1
        q = deque([(i, j)])
        while q:
            y, x = q.popleft()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < M and original_grid[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    grid[ny][nx] = grid[i][j]
                    q.append((ny, nx))

edges = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == -1:
            continue
        for k in range(4):
            y, x = i + dy[k], j + dx[k]
            dist = 0
            while 0 <= y < N and 0 <= x < M and grid[y][x] == -1:
                y += dy[k]
                x += dx[k]
                dist += 1
            if dist < 2 or (not 0 <= y < N) or (not 0 <= x < M) or grid[y][x] == grid[i][j]:
                continue
            edges.append((dist, grid[i][j], grid[y][x]))

ans = kruskal(comp, edges)
if not ans:
    print(-1)
else:
    print(ans)
