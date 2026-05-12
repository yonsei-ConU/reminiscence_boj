import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


ans = 1
def dfs(g, v, alpha, cnt):
    global ans
    x, y = v
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < len(g) and 0 <= ny < len(g[0])):
            continue
        next_alpha = ord(g[nx][ny]) - 65
        if not alpha & (1 << next_alpha):
            ans = max(ans, cnt + 1)
            dfs(g, (nx, ny), alpha | (1 << next_alpha), cnt + 1)


R, C = minput()
board = [list(input_().strip()) for _ in range(R)]
alpha = 0
alpha += 1 << (ord(board[0][0]) - 65)
dfs(board, (0, 0), alpha, 1)
print(ans)
