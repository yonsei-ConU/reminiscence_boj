import sys
from algorithms import matrix_mult, matrix_pow
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10 ** 9 + 7
T, N, D = minput()
maps = []
for _ in range(T):
    tempmap = [[0] * N for _ in range(N)]
    for __ in range(int(input_())):
        a, b, c = minput()
        a -= 1; b -= 1
        tempmap[a][b] = c
    maps.append(tempmap)

cycle = maps[0]
for i in range(1, T):
    cycle = matrix_mult(cycle, maps[i], MOD)

q, r = divmod(D, T)
ans = matrix_pow(cycle, q, MOD)
for i in range(r):
    ans = matrix_mult(ans, maps[i], MOD)

for a in ans: print(*a)
