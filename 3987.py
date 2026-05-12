# 13m 30.41s

import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


# 아래 위 오른쪽 왼쪽
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = minput()
g = [list(input_().rstrip()) for _ in range(N)]
PR, PC = minput()
ans_time = 0
ans_val = ''

for direction in [1, 2, 0, 3]:
    y, x = PR - 1, PC - 1
    time = 0
    d = direction
    visited = [[[False, False, False, False] for __ in range(M)] for _ in range(N)]
    visited[y][x][d] = True
    while True:
        time += 1
        ny, nx = y + dy[d], x + dx[d]
        if not (0 <= ny < N and 0 <= nx < M) or g[ny][nx] == 'C':
            break
        elif visited[ny][nx][d]:
            time = float('inf')
            break
        elif g[ny][nx] == '/':
            visited[ny][nx][d] = True
            d = 3 - d
        elif g[ny][nx] == '\\':
            visited[ny][nx][d] = True
            d = (d + 2) % 4
        y, x = ny, nx
        visited[y][x][d] = True
    if time == float('inf'):
        ans_val = direction
        ans_time = 'Voyager'
        break
    elif time > ans_time:
        ans_val = direction
        ans_time = time

print('DURL'[ans_val])
print(ans_time)
