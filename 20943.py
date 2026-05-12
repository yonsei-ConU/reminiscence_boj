import sys
from fractions import Fraction
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
incl = defaultdict(int)
for _ in range(N):
    a, b, c = minput()
    if not a:
        incl[10 ** 18] += 1
    else:
        incl[Fraction(b, a)] += 1

ans = 0
for v in incl.values():
    ans += v * (N - v)

print(ans // 2)
