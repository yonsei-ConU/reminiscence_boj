import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
diff = [[0] * 1002 for _ in range(1002)]
for _ in range(N):
    x1, y1, x2, y2 = minput()
    diff[x1][y1] += 1
    diff[x1][y2] -= 1
    diff[x2][y1] -= 1
    diff[x2][y2] += 1

ps1 = [[0] * 1002 for _ in range(1002)]
for i in range(1002):
    cur_sum = 0
    for j in range(1002):
        cur_sum += diff[i][j]
        ps1[i][j] = cur_sum

ps2 = [[0] * 1002 for _ in range(1002)]
for j in range(1002):
    cur_sum = 0
    for i in range(1002):
        cur_sum += ps1[i][j]
        ps2[i][j] = cur_sum

ans = 0
for i in range(1001):
    for j in range(1001):
        if ps2[i][j] == K:
            ans += 1

print(ans)
