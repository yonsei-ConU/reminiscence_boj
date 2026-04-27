import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def bs(lst, v):
    lo = -1
    hi = len(lst)
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if lst[mid] <= v:
            lo = mid
        else:
            hi = mid
    if lo == -1:
        return -99999999999999999999
    return lst[lo]


N, D = minput()
A = defaultdict(int)
B = defaultdict(int)
ans = 0
for _ in range(N):
    t, a, b = minput()
    A[t] = max(A[t], a)
    B[t] = max(B[t], b)
    ans = max(ans, a + b)

mA = 0
ak = sorted(list(A.keys()))
for v in ak:
    mA = max(mA, A[v])
    A[v] = max(A[v], mA)

mB = 0
bk = sorted(list(B.keys()))
for v in bk:
    mB = max(mB, B[v])
    B[v] = max(B[v], mB)

for v in ak:
    ans = max(ans, A[v] + B[bs(bk, D - v)])
for v in bk:
    ans = max(ans, B[v] + A[bs(ak, D - v)])

print(ans)
