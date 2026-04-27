import sys
from math import sqrt, pi
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def convex_hull(points):
    if len(points) < 3: return points
    ccw = lambda p1, p2, p3: p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]
    points.sort()
    ret_down = [points[0], points[1]]
    for p in points:
        while len(ret_down) > 1 and ccw(ret_down[-2], ret_down[-1], p) <= 0:
            ret_down.pop()
        ret_down.append(p)

    ret_up = [points[-1], points[-2]]
    for p in points[::-1]:
        while len(ret_up) > 1 and ccw(ret_up[-2], ret_up[-1], p) <= 0:
            ret_up.pop()
        ret_up.append(p)

    return ret_up[:-1] + ret_down[:-1]


N, L = minput()
points = [tuple(minput()) for _ in range(N)]
hull = convex_hull(points)
perimeter = 0
N = len(hull)
for i in range(N - 1):
    perimeter += sqrt((hull[i][0] - hull[i + 1][0]) ** 2 + (hull[i][1] - hull[i + 1][1]) ** 2)
perimeter += sqrt((hull[N - 1][0] - hull[0][0]) ** 2 + (hull[N - 1][1] - hull[0][1]) ** 2)
ans = perimeter + 2 * L * pi
print(round(ans))
