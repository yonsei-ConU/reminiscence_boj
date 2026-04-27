import sys
from bisect import bisect_left as bs_left
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
a = list(minput())
a_orig = a[:]

a.sort()
a_rank = {a[i]: i for i in range(N)}

original_sum = 0
cur_sum = 0
ps = [0]

for i in range(N):
    cur_sum += a[i]
    original_sum += a[i] * (i + 1)
    ps.append(cur_sum)

for _ in range(int(input_())):
    i, j = minput()
    i -= 1
    rank = a_rank[a_orig[i]]
    new_rank = bs_left(a, j)
    if new_rank < rank or (new_rank == rank and a_orig[i] > j):
        print(original_sum - ((rank + 1) * a_orig[i] - (new_rank + 1) * j) + ps[rank] - ps[new_rank])
    else:
        print(original_sum - ((rank + 1) * a_orig[i] - new_rank * j) + ps[rank + 1] - ps[new_rank])
