import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from collections import deque
from time import sleep

N = int(input_())
g = []
for i in range(N):
    l = list(minput())
    if 9 in l:
        j = l.index(9)
        l[j] = 0
        now = (i, j)
    g.append(l)

size = 2
fish = 0
time = 0
dy = [ -1,  1,  0,  0]
dx = [  0,  0, -1,  1]

while True:
    q = deque((now,))
    dist = [[-1] * N for _ in range(N)]
    dist[now[0]][now[1]] = 0
    max_dist = 987654321
    next_fish = (N, N)
    while q:
        y, x = q.popleft()
        if dist[y][x] >= max_dist:
            break
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if g[ny][nx] in (0, size) and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
            elif 0 < g[ny][nx] < size and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
                max_dist = dist[y][x] + 1
                if ny < next_fish[0]:
                    next_fish = (ny, nx)
                elif ny == next_fish[0]:
                    if nx < next_fish[1]:
                        next_fish = (ny, nx)
    else:
        print(time)
        break
    g[next_fish[0]][next_fish[1]] = 0
    time += max_dist
    now = next_fish[:]
    fish += 1
    if fish == size:
        fish = 0
        size += 1
