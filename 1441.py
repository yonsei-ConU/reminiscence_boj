import sys
from math import lcm
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, L, R = minput()
A = list(minput())
ans = 0

for mask in range(1, 1 << N):
    sign = [-1, 1][mask.bit_count() & 1]
    lst = []
    for i in range(N):
        if mask & (1 << i):
            lst.append(A[i])
    x = lcm(*lst)
    ans += sign * (R // x - (L - 1) // x)

print(ans)
