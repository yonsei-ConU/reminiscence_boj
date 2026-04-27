import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
B = list(minput())
d = defaultdict(list)
for i in range(N):
    x = B[i]
    three = 0
    while not x % 3:
        three += 1
        x //= 3
    d[three].append(B[i])

d_keys = sorted(d.keys(), reverse=True)
for key in d_keys:
    l = d[key]
    print(*sorted(l), end=' ')
print()
