import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
original = [list(minput()) for _ in range(N)]
delta = [[0] * N for _ in range(N)]

for _ in range(int(input_())):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input_().split())
    delta[y1][x1] += 1
    if y2 + 1 < N:
        delta[y2 + 1][x1] -= 1
    if x2 + 1 < N:
        delta[y1][x2 + 1] -= 1
    if y2 + 1 < N and x2 + 1 < N:
        delta[y2 + 1][x2 + 1] += 1

ps1 = [[0] * N for _ in range(N)]
for i in range(N):
    cur_sum = 0
    for j in range(N):
        cur_sum += delta[i][j]
        ps1[i][j] = cur_sum

ps2 = [[0] * N for _ in range(N)]
for j in range(N):
    cur_sum = 0
    for i in range(N):
        cur_sum += ps1[i][j]
        ps2[i][j] = cur_sum

ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans[i][j] = (original[i][j] + ps2[i][j]) & 1

for a in ans: print(*a)
