import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
direction = {'D': 0, 'U': 1, 'R': 2, 'L': 3}
N, M = minput()
g = []
ans_coordinates = []
robot = ()
for i in range(N):
    s = input_().rstrip()
    j = s.find('S')
    if j != -1: robot = (i, j)
    tmp = [j for j in range(M) if s[j] == '.']
    for j in tmp: ans_coordinates.append((i, j))
    g.append(list(s))

ans = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if g[i][j] == 'C':
            for k in range(4):
                y, x = i, j
                while True:
                    y, x = y + dy[k], x + dx[k]
                    if g[y][x] == '.':
                        g[y][x] = 'W'
                    elif g[y][x] == 'S':
                        for i in range(len(ans_coordinates)):
                            print(-1)
                        exit()
                    elif g[y][x] in 'UDLR':
                        pass
                    else:
                        break

q = deque([robot])
y, x = robot
ans[y][x] = 0
while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ans[ny][nx] != -1 or g[ny][nx] in 'WC': continue
        if g[ny][nx] == '.':
            q.append((ny, nx))
            ans[ny][nx] = ans[y][x] + 1
        else:
            visited = {(ny, nx)}
            flag = True
            while True:
                d = direction[g[ny][nx]]
                ny, nx = ny + dy[d], nx + dx[d]
                if (ny, nx) in visited or g[ny][nx] in 'WCS':
                    flag = False
                    break
                elif g[ny][nx] == '.':
                    break
                visited.add((ny, nx))
            if flag and ans[ny][nx] == -1:
                q.append((ny, nx))
                ans[ny][nx] = ans[y][x] + 1

for y, x in ans_coordinates:
    print(ans[y][x])
