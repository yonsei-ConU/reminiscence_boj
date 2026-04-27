import sys
from math import gcd
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) << 1, input_().split())


def get_incl(dy, dx):
    if dx < 0:
        dy *= -1
        dx *= -1
    if not dy:
        dx = 1
    elif not dx:
        dy = 1
    else:
        g = gcd(dx, dy)
        dy //= g
        dx //= g
    return dy, dx


N = int(input_())
points = [list(minput()) for _ in range(N)]
ans = 0

for i in range(N):
    incl = defaultdict(int)
    for j in range(N):
        if i == j:
            continue
        dy = points[j][1] - points[i][1]
        dx = points[j][0] - points[i][0]
        dy, dx = get_incl(dy, dx)
        incl[(dx, dy)] += 1
    for j in range(N):
        if i == j:
            continue
        dy = points[j][1] - points[i][1]
        dx = points[j][0] - points[i][0]
        dy, dx = get_incl(dy, dx)
        ans += incl[(-dy, dx)]

print(ans)
