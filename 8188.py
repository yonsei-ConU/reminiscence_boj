import sys
from collections import defaultdict
from bisect import bisect_right as upper_bound
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


M = int(input_())
a = list(minput())
a_rev = defaultdict(list)
for i in range(M): a_rev[a[i]].append(i)

n = int(input_())
for _ in range(n):
    m = int(input_())
    b = list(minput())
    ptr = -1
    ans = 'TAK'
    for item in b:
        upb = upper_bound(a_rev[item], ptr)
        if upb == len(a_rev[item]):
            ans = 'NIE'
            break
        else:
            ptr = a_rev[item][upb]
    print(ans)
