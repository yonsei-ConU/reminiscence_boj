import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, m = minput()
    cur = n * m
    res = [[0] * m for _ in range(n)]
    for i in range(2, m + n + 1):
        for j in range(1, i):
            x, y = j - 1, i - j - 1
            if 0 <= x < n and 0 <= y < m:
                res[x][y] = cur
                cur -= 1
    for r in res: print(*r)
