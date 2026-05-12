import sys
from algorithms import manacher
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
pal = manacher(A)
for _ in range(int(input_())):
    S, E = minput()
    S -= 1; E -= 1
    S = 2 * S + 1
    E = 2 * E + 1
    mid = (S + E) >> 1
    if pal[mid] >= mid - S + 1:
        print(1)
    else:
        print(0)
