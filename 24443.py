import sys
import bisect
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, Q = minput()
rN = isqrt(N) * 2
A = list(minput())
buckets = []
sorted_buckets = []

i = 0
while i < N:
    lst = A[i:i + rN]
    buckets.append(lst)
    sorted_buckets.append(sorted(lst))
    i += rN

for _ in range(Q):
    query = list(minput())
    if query[0] == 1:
        i, j, k = query[1:]
        i -= 1
        j -= 1
        x = i // rN
        y = j // rN

        lo = min(A) - 1
        hi = max(A) + 1

        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            cnt = 0
            for z in range(x + 1, y):
                cnt += bisect.bisect_right(sorted_buckets[z], mid)
            if x == y:
                for val in buckets[x][i % rN : j % rN + 1]:
                    if val <= mid:
                        cnt += 1
            else:
                for val in buckets[x][i % rN:]:
                    if val <= mid:
                        cnt += 1
                for val in buckets[y][:j % rN + 1]:
                    if val <= mid:
                        cnt += 1
            if cnt >= k:
                hi = mid
            else:
                lo = mid
        print(hi)
    else:
        i, j = query[1:]
        i -= 1
        j -= 1
        if i == j:
            continue
        xi = i // rN
        yi = j // rN
        xi_pos = i % rN
        yi_pos = j % rN
        val_i = buckets[xi][xi_pos]
        val_j = buckets[yi][yi_pos]
        buckets[xi][xi_pos], buckets[yi][yi_pos] = val_j, val_i
        sorted_buckets[xi].remove(val_i)
        bisect.insort(sorted_buckets[xi], val_j)
        sorted_buckets[yi].remove(val_j)
        bisect.insort(sorted_buckets[yi], val_i)
