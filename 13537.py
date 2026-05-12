import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
rN = isqrt(N)
A = list(minput())
buckets = []
sorted_buckets = []

i = 0
while i < N:
    lst = A[i:i + rN]
    buckets.append(lst)
    sorted_buckets.append(sorted(lst))
    i += rN

M = int(input_())
for _ in range(M):
    i, j, k = minput()
    i -= 1
    j -= 1
    x = i // rN
    y = j // rN
    ans = 0
    for z in range(x + 1, y):
        lo = -1
        hi = rN
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if sorted_buckets[z][mid] > k:
                hi = mid
            else:
                lo = mid
        ans += rN - hi
    if x != y:
        bx = buckets[x]
        xmod = i % rN
        for z in bx[xmod:]:
            if z > k:
                ans += 1
        by = buckets[y]
        ymod = j % rN
        for z in by[:ymod + 1]:
            if z > k:
                ans += 1
    else:
        bx = buckets[x]
        xmod = i % rN
        ymod = j % rN
        for z in bx[xmod:ymod + 1]:
            if z > k:
                ans += 1
    print(ans)
