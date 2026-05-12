import sys
from functools import cmp_to_key
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]


def angle_sort(points, center):
    new_pts = []
    for p in points:
        if p != center:
            new_pts.append(p)
    def cmp(a, b):
        if (a < center) == (b < center):
            c = ccw(center, a, b)
            if c > 0:
                return -1
            elif c < 0:
                return 1
            else:
                return 0
        elif a < b:
            return -1
        else:
            return 1

    return sorted(new_pts, key=cmp_to_key(cmp))


def nC4(n):
    return n * (n - 1) * (n - 2) * (n - 3) // 24


def nC3(n):
    return n * (n - 1) * (n - 2) // 6


N = int(input_())
if N < 5:
    exit(print(0))
points = [list(minput()) for _ in range(N)]
ans = 0
for center in points:
    sp = angle_sort(points, center)
    tmp = nC4(N - 1) << 1
    r = 0
    for l in range(N - 1):
        if l == r:
            r += 1
        while ccw(center, sp[l], sp[r % (N - 1)]) > 0:
            r += 1
        d = r - l
        tmp -= nC3(d - 1)
    ans += tmp

print(ans)
