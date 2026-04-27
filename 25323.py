import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
B = sorted(A)
chk = True
for i in range(N):
    t = A[i] * B[i]
    if isqrt(t) ** 2 != t:
        chk = False
        break

if chk:
    print("YES")
else:
    print("NO")
