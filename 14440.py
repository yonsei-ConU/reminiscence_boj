import sys
from algorithms import matrix_pow, matrix_mult
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def prt(x):
    if x < 10:
        print('0' + str(x))
    else:
        print(x)


x, y, a0, a1, n = minput()
if n == 0:
    exit(prt(a0))
elif n == 1:
    exit(prt(a1))
mod = 100
pw = matrix_pow([[x, y], [1, 0]], n - 1, 100)
ans = matrix_mult(pw, [[a1], [a0]], 100)[0][0]
prt(ans)
