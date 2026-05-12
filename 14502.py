import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from itertools import combinations
from collections import deque

N, M = minput()
board = []
empty = []
virus = []

for i in range(N):
    l = list(minput())
    board.append(l)
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

ans = -1
for c in combinations(empty, 3):
    q = deque(virus)
    cnt = len(empty) - 3
    visited = [[False] * M for _ in range(N)]
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and (nx, ny) not in c and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt -= 1
    ans = max(cnt, ans)
print(ans)
