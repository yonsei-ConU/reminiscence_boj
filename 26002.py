import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
h, w = minput()
a = [list(minput()) for _ in range(h)]
ans = [[-1] * w for _ in range(h)]
for si in range(h):
    for sj in range(w):
        for ei in range(h):
            for ej in range(w):
                if si == ei and sj == ej:
                    continue
                if si == 0 and sj == 0 and ei == 2 and ej == 2:
                    1
                ev = a[ei][ej]
                dist = [[-1] * w for _ in range(h)]
                dist[si][sj] = 0
                y = si
                x = sj
                while True:
                    if y == ei and x == ej:
                        break
                    min_idx = -1
                    min_val = (10 ** 18, 0)
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if not 0 <= ny < h or not 0 <= nx < w:
                            continue
                        if abs(a[ny][nx] - ev) < min_val[0] or (abs(a[ny][nx] - ev) == min_val[0] and abs(a[ny][nx] - a[y][x]) < min_val[1]):
                            min_idx = i
                            min_val = (abs(a[ny][nx] - ev), abs(a[ny][nx] - a[y][x]))
                    ny = y + dy[min_idx]
                    nx = x + dx[min_idx]
                    if min_idx == -1 or dist[ny][nx] != -1:
                        break
                    dist[ny][nx] = dist[y][x] + 1
                    y = ny
                    x = nx
                if dist[ei][ej] != -1:
                    ans[si][sj] = max(ans[si][sj], dist[ei][ej])
                else:
                    ans[si][sj] = 10 ** 18
ans_idx = -1
ans_val = 10 ** 18
for i in range(h):
    for j in range(w):
        if ans[i][j] != -1 and ans[i][j] < ans_val:
            ans_idx = a[i][j]
            ans_val = ans[i][j]
if ans_idx == -1:
    print("impossible")
else:
    print(ans_idx, ans_val)
