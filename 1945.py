import sys
from functools import cmp_to_key
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def angle_sort(points, center):
    def ccw(p1, p2, p3):
        return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]

    def cmp(a, b):
        if (a < center) == (b < center):
            c = ccw(center, a, b)
            if c > 0:
                return -1
            elif c < 0:
                return 1
            else:
                if a[2] == 1:
                    return -1
                if b[2] == 1:
                    return 1
                return 0
        elif a < b:
            return -1
        else:
            return 1

    return sorted(points, key=cmp_to_key(cmp))


N = int(input_())
points = []
for i in range(N):
    x1, y1, x2, y2 = minput()
    points.append([x2, y1, 1])
    points.append([x1, y2, -1])

points = angle_sort(points, [0, 0])
ans = 0
cur_sum = 0

for p in points:
    cur_sum += p[2]
    ans = max(ans, cur_sum)

print(ans)
