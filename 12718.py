import sys
from math import comb
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    n, A, B, C, D, x, y, M = minput()
    mod3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(n):
        mod3[x % 3][y % 3] += 1
        x = (A * x + B) % M
        y = (C * y + D) % M
    ans = mod3[0][0] * mod3[0][1] * mod3[0][2] + mod3[0][0] * mod3[1][0] * mod3[2][0] + mod3[1][0] * mod3[1][1] * mod3[1][2] + mod3[0][1] * mod3[1][1] * mod3[2][1] + mod3[2][0] * mod3[2][1] * mod3[2][2] + mod3[0][2] * mod3[1][2] * mod3[2][2] + mod3[0][0] * mod3[1][1] * mod3[2][2] + mod3[0][0] * mod3[1][2] * mod3[2][1] + mod3[0][1] * mod3[1][0] * mod3[2][2] + mod3[0][1] * mod3[1][2] * mod3[2][0] + mod3[0][2] * mod3[1][0] * mod3[2][1] + mod3[0][2] * mod3[1][1] * mod3[2][0]

    for i in range(3):
        for j in range(3):
            if mod3[i][j] >= 3:
                ans += comb(mod3[i][j], 3)
    print(f"Case #{tc}: {ans}")
