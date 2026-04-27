import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
CS, E = minput()
res = [['0'] * N for _ in range(N)]
cnt = 0
for i in range(N - 1):
    for j in range(N - 1 - i):
        if cnt < CS:
            res[i][j] = '1'
        if cnt < E:
            res[N - 1 - i][N - 1 - j] = '2'
        cnt += 1

if cnt < CS and cnt < E: exit(print(-1))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

y = 0
x = N - 1
while cnt < CS:
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < N and res[ny][nx] == '2':
            break
    else:
        res[y][x] = '1'
        cnt += 1
    x += 1
    if x == N:
        y += 1
        if y == N: exit(print(-1))
        x = N - 1 - y

x = 0
y = N - 1
while cnt < E:
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < N and res[ny][nx] == '1':
            break
    else:
        res[y][x] = '2'
        cnt += 1
    x -= 1
    if x == -1:
        y -= 1
        if y == -1: exit(print(-1))
        x = N - 1 - y

print(1)
for r in res: print(*r)
