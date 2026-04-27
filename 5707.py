import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
while True:
    N, R, C, K = minput()
    if not N:
        break
    prev = [list(minput()) for _ in range(R)]

    for _ in range(K):
        g = [[-1] * C for _ in range(R)]
        for i in range(N):
            q = []
            for y in range(R):
                for x in range(C):
                    if prev[y][x] == i:
                        q.append((y, x))
            while q:
                y, x = q.pop()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < R and 0 <= nx < C and prev[ny][nx] == (i + 1) % N and g[ny][nx] == -1:
                        g[ny][nx] = i
        for y in range(R):
            for x in range(C):
                if g[y][x] == -1:
                    g[y][x] = prev[y][x]
        g, prev = prev, g

    for row in prev: print(*row)
