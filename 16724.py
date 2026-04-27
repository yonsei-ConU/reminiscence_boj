import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g = []
for _ in range(N): g.append(input_().rstrip())
cycle = [[-1] * M for _ in range(N)]
idx = 0
ans = 0
for i in range(N):
    for j in range(M):
        if cycle[i][j] == -1:
            y, x = i, j
            cycle[y][x] = idx
            check = False
            while 1:
                direction = g[y][x]
                if direction == 'U':
                    ny, nx = y - 1, x
                elif direction == 'D':
                    ny, nx = y + 1, x
                elif direction == 'L':
                    ny, nx = y, x - 1
                else:
                    ny, nx = y, x + 1
                if cycle[ny][nx] == -1:
                    cycle[ny][nx] = idx
                    y, x = ny, nx
                elif cycle[ny][nx] == idx:
                    check = True
                    break
                else:
                    break
            if check:
                ans += 1
            idx += 1

print(ans)
