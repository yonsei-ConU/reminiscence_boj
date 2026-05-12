import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def query(y1, y2, x1, x2):
    return psum[x2 + 1][y2 + 1] - psum[x1][y2 + 1] - psum[x2 + 1][y1] + psum[x1][y1]


N = int(input_())
matrix = [input_().rstrip() for _ in range(N)]
psum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + int(matrix[i - 1][j - 1])

ans = 0
ok = set()
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            ok.add((i, j))
for sz in range(3, N + 1, 2):
    new_ok = set()
    for y, x in ok:
        y -= sz // 2
        x -= sz // 2
        if y < 0 or x < 0 or y + sz > N or x + sz > N: continue
        if query(y + sz // 2, y + sz // 2, x, x + sz - 1) == query(y, y + sz - 1, x + sz // 2, x + sz // 2) == sz and query(y, y + sz // 2 - 1, x, x + sz // 2 - 1) == query(y, y + sz // 2 - 1, x + sz // 2 + 1, x + sz - 1) == query(y + sz // 2 + 1, y + sz - 1, x, x + sz // 2 - 1) == query(y + sz // 2 + 1, y + sz - 1, x + sz // 2 + 1, x + sz - 1) == 0:
            new_ok.add((y + sz // 2, x + sz // 2))
    ans += len(new_ok)
    ok, new_ok = new_ok, ok

print(ans)
