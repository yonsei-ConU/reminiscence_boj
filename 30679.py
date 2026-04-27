import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
N, M = minput()
g = [list(minput()) for _ in range(N)]
ans = []

for init_y in range(N):
    y = init_y
    x = 0
    direction = 0
    visited = {(y, x, direction)}
    while True:
        ny, nx = y + dy[direction] * g[y][x], x + dx[direction] * g[y][x]
        if not (0 <= ny < N and 0 <= nx < M):
            chk = False
            break
        direction = (direction + 1) % 4
        if (ny, nx, direction) in visited:
            chk = True
            break
        visited.add((ny, nx, direction))
        y, x = ny, nx
    if chk:
        ans.append(init_y + 1)

print(len(ans))
if ans:
    print(*ans)
