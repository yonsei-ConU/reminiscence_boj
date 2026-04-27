import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
field = []
for i in range(12): field.append(list(input_().rstrip()))
ans = 0

while True:
    # check what to remove
    visited = [[False] * 6 for _ in range(12)]
    to_delete = []
    for i in range(12):
        for j in range(6):
            if not visited[i][j]:
                visited[i][j] = True
                color = field[i][j]
                if color == '.': continue
                q = deque([(i, j)])
                cur_component =[(i, j)]
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx] and field[ny][nx] == color:
                            q.append((ny, nx))
                            cur_component.append((ny, nx))
                            visited[ny][nx] = True
                if len(cur_component) >= 4:
                    for c in cur_component: to_delete.append(c[:])
    # exit condition
    if not to_delete:
        break
    # remove
    ans += 1
    for y, x in to_delete:
        field[y][x] = '.'
    # fall
    for x in range(6):
        column = []
        for y in range(11, -1, -1):
            if field[y][x] != '.':
                column.append(field[y][x])
        for i in range(11):
            if i < len(column):
                field[11 - i][x] = column[i]
            else:
                field[11 - i][x] = '.'

print(ans)
