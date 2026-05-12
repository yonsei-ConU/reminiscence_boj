import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    x, y = minput()
    d = y - x
    # i번의 이동으로 갈 수 있는 거리의 최댓값은 (i + 2) // 2 + (i + 3) // 2
    rd = isqrt(d)
    ans = 2 * rd
    if rd * rd == d:
        ans -= 1
    elif d <= rd * (rd + 1):
        ans += 0
    else:
        ans += 1
    print(ans)
