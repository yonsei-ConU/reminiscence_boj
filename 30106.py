import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M, K = minput()
g = [tuple(minput()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ans = 0
for sy in range(N):
    for sx in range(M):
        if visited[sy][sx]:
            continue
        ans += 1
        visited[sy][sx] = True
        q = deque([(sy, sx)])
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if not (0 <= ny < N and 0 <= nx < M) or visited[ny][nx] or abs(g[ny][nx] - g[y][x]) > K:
                    continue
                visited[ny][nx] = True
                q.append((ny, nx))
                
print(ans)
