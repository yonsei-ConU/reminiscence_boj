import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X, Y, c = minput()
dist = X ** 2 + Y ** 2
c *= c
ans = isqrt(dist // c)
if ans ** 2 * c ^ dist:
    ans += 1
if not dist:
    ans = 0
elif dist < c:
    ans = 2

print(ans)
