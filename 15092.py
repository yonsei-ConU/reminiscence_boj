import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
m, n = minput()
g = [input_().rstrip() for _ in range(m)]
visited = [[False] * n for _ in range(m)]
ans = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] or g[i][j] == '.':
            continue
        ans += 1
        visited[i][j] = True
        chk = True
        y = i
        x = j
        while chk:
            for k in range(8):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < m and 0 <= nx < n and g[ny][nx] == '#' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    y, x = ny, nx
                    break
            else:
                chk = False

print(ans)
