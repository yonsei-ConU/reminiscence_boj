import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
ans = [[0] * M for _ in range(N)]
ans[0][1] = 1
ans[1][0] = 2
ans[1][1] = 3
ans[1][2] = 4
ans[2][1] = 5
for cy in range(1, N - 1):
    if cy != 1:
        ans[cy][0] = ans[cy - 2][1]
        ans[cy][2] = ans[cy - 1][0]
        ans[cy + 1][1] = ans[cy - 1][2]
    for cx in range(2, M - 1):
        ans[cy][cx + 1] = ans[cy - 1][cx - 1]
        ans[cy - 1][cx] = ans[cy + 1][cx - 1]
        ans[cy + 1][cx] = ans[cy][cx - 2]

ans[0][0] = 1
if ans[0][1] <= 2:
    ans[0][0] = ans[0][1] + 1
if ans[1][0] == ans[0][0]:
    ans[0][0] += 1
ans[0][-1] = 1
if ans[0][-2] <= 2:
    ans[0][-1] = ans[0][-2] + 1
if ans[1][-1] == ans[0][-1]:
    ans[0][-1] += 1
ans[-1][0] = 1
if ans[-2][0] <= 2:
    ans[-1][0] = ans[-2][0] + 1
if ans[-1][1] == ans[-1][0]:
    ans[-1][0] += 1
ans[-1][-1] = 1
if ans[-1][-2] <= 2:
    ans[-1][-1] = ans[-1][-2] + 1
if ans[-2][-1] == ans[-1][-1]:
    ans[-1][-1] += 1
for a in ans:
    print(*a)
