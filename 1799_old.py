import sys
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


n = int(input_())
chess = [list(minput()) for _ in range(n)]
cnt = 1
d1 = [[0] * n for _ in range(n)]
d2 = [[0] * n for _ in range(n)]
dinfo = [[] for _ in range(n ** 2)]

for i in range(2 * n - 1):
    t = i - n + 1
    check = False
    for j in range(max(0, t), min(n, n + t)):
        x, y = j, j - t
        d1[x][y] = cnt
        if chess[x][y]:
            dinfo[cnt].append(n * x + y)
            check = True
    cnt += 1

for i in range(2 * n - 1):
    for j in range(max(0, i - n + 1), min(n, i + 1)):
        x, y = j, i - j
        d2[x][y] = cnt
        if chess[x][y]:
            dinfo[cnt].append(n * x + y)
    cnt += 1
for d in d1: print(*d)
print()
for d in d2: print(*d)
print()
for d in dinfo: print(*d)
