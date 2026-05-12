import sys
from math import sqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, x = minput()
a = list(minput())
if a.count(0) == n:
    print(*a)
    exit()
square_sum = sum(v ** 2 for v in a) / n
print(*[v / sqrt(square_sum) * sqrt(x) for v in a])
