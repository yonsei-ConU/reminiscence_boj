import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


m, n = minput()
board = [list(map(int, list(input_().strip()))) for _ in range(m)]
cnt1 = 0
cnt2 = 0
for k in range(m):
    for l in range(n):
        if (k + l) % 2:
            if board[k][l] == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if board[k][l] == 2:
                cnt1 += 1
            else:
                cnt2 += 1
print(min(cnt1, cnt2))
