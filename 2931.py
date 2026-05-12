import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def simulate_gas(initial_position):
    global block_cnt
    y, x = initial_position
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not (0 <= ny < R and 0 <= nx < C): continue
        elif g[ny][nx] == '.' or g[ny][nx] == 'M' or g[ny][nx] == 'Z': continue
        else: break
    else:
        1 / 0
    direction = i
    y, x = ny, nx
    while True:
        if g[y][x] == '-' or g[y][x] == '|' or g[y][x] == '+':
            pass
        elif g[y][x] == '1' or g[y][x] == '3':
            direction = 3 - direction
        elif g[y][x] == '2' or g[y][x] == '4':
            direction = (direction + 2) % 4
        else:
            if g[y][x] != '.':
                assert False
            return y, x, direction
        y += dy[direction]
        x += dx[direction]
        block_cnt -= 1


# 아래 0 위 1 오른쪽 2 왼쪽 3
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
R, C = minput()
g = []
M = ()
Z = ()
block_cnt = 0
for i in range(R):
    row = input_().rstrip()
    tmp = C
    for j in range(C):
        if row[j] == 'M':
            M = (i, j)
            tmp -= 1
        elif row[j] == 'Z':
            Z = (i, j)
            tmp -= 1
    block_cnt += tmp - row.count('.') + row.count('+')
    g.append(row)

My, Mx, Md = simulate_gas(M)
Zy, Zx, Zd = simulate_gas(Z)
if not (My == Zy and Mx == Zx and block_cnt >= 0):
    import aoiwurdfhjsk
ans_block = ''
if block_cnt:
    ans_block = '+'
elif (Md == 2 and Zd == 3) or (Md == 3 and Zd == 2):
    ans_block = '-'
elif (Md == 0 and Zd == 1) or (Md == 1 and Zd == 0):
    ans_block = '|'
elif (Md == 1 and Zd == 3) or (Md == 3 and Zd == 1):
    ans_block = '1'
elif (Md == 0 and Zd == 3) or (Md == 3 and Zd == 0):
    ans_block = '2'
elif (Md == 0 and Zd == 2) or (Md == 2 and Zd == 0):
    ans_block = '3'
elif (Md == 1 and Zd == 2) or (Md == 2 and Zd == 1):
    ans_block = '4'
else:
    print(int('awiuehfjsdk'))
print(My + 1, Zx + 1, ans_block)
"""
3 5
..1-M
1-.4.
Z.23."""
