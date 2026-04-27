import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from collections import deque

N, M = minput()
g = []
building_count = 0
for i in range(N):
    s = input_().rstrip()
    for j in range(M):
        if s[j] == '@':
            start = (i, j)
        elif s[j] == '*':
            building_count += 1
        elif s[j] == '#':
            building_count += 1
    g.append(list(s))

fallen = 0
q = deque([(start[0], start[1])])
while q:
    y, x = q.popleft()
    if (y, x) == start:
        dy = [-1, -2, 1, 2,  0,  0, 0, 0]
        dx = [ 0,  0, 0, 0, -1, -2, 1, 2]
    else:
        dy = [-1, 1,  0, 0]
        dx = [ 0, 0, -1, 1]
    cont = False
    for i in range(len(dy)):
        if abs(dy[i]) == 1 or abs(dx[i]) == 1:
            cont = False
        if cont:
            continue
        if not (0 <= y + dy[i] < N and 0 <= x + dx[i] < M):
            continue
        nxt = g[y + dy[i]][x + dx[i]]
        if nxt == '*':
            q.append((y + dy[i], x + dx[i]))
            g[y + dy[i]][x + dx[i]] = '.'
            fallen += 1
        elif nxt == '#':
            g[y + dy[i]][x + dx[i]] = '*'
        elif nxt == '|':
            cont = True

print(fallen, building_count - fallen)
