import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
chk = [[True] * m for _ in range(n)]
occupied = [[False] * m for _ in range(n)]
Q, *q = minput()
K, *k = minput()
P, *p = minput()
queen = []
knight = []
pawn = []
ptr = 0
while ptr < len(q):
    y = q[ptr] - 1
    x = q[ptr + 1] - 1
    ptr += 2
    chk[y][x] = False
    occupied[y][x] = True
    queen.append((y, x))
ptr = 0
while ptr < len(k):
    y = k[ptr] - 1
    x = k[ptr + 1] - 1
    ptr += 2
    chk[y][x] = False
    occupied[y][x] = True
    knight.append((y, x))
ptr = 0
while ptr < len(p):
    y = p[ptr] - 1
    x = p[ptr + 1] - 1
    ptr += 2
    chk[y][x] = False
    occupied[y][x] = True
    pawn.append((y, x))

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
for y, x in queen:
    for i in range(8):
        cy, cx = y + dy[i], x + dx[i]
        while 0 <= cy < n and 0 <= cx < m and not occupied[cy][cx]:
            chk[cy][cx] = False
            cy, cx = cy + dy[i], cx + dx[i]

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [2, 1, -1, -2, -2, -1, 1, 2]
for y, x in knight:
    for i in range(8):
        if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m:
            chk[y + dy[i]][x + dx[i]] = False

print(sum(sum(x) for x in chk))
