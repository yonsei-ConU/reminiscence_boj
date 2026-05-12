import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def convex_hull(points):
    if len(points) < 3:
        return points
    if len(points) == 3:
        if ccw(points[0], points[1], points[2]) < 0:
            return points[::-1]
        else:
            return points
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


def polygon_area_2(points):
    area = 0
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        area += p1[0] * p2[1] - p1[1] * p2[0]
    return abs(area)


def point_in_convex_polygon(p, polygon):
    rlwns = polygon[0]
    lo = 0
    hi = len(polygon)
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        t = ccw(rlwns, polygon[mid], p)
        if t > 0:
            lo = mid
        elif t < 0:
            hi = mid
        else:
            if ((p[0] - rlwns[0]) ** 2 + (p[1] - rlwns[1]) ** 2 <= (polygon[mid][0] - rlwns[0]) ** 2 + (polygon[mid][1] - rlwns[1]) ** 2) and ((p[0] - polygon[mid][0]) ** 2 + (p[1] - polygon[mid][1]) ** 2 <= (polygon[mid][0] - rlwns[0]) ** 2 + (polygon[mid][1] - rlwns[1]) ** 2):
                return True
            else:
                return False
    if not lo or hi == len(polygon):
        return False
    return ccw(polygon[lo], polygon[hi], p) >= 0


def ccw(p1, p2, p3): return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]


N, M = minput()
polygon = convex_hull([list(minput()) for _ in range(N)])
H = len(polygon)
if H == 1:
    assert M == 1
    exit(print(+(list(minput()) != polygon[0])))
elif H == 2:
    x1, y1 = polygon[0]
    x2, y2 = polygon[1]
    if x2 < x1: x1, x2 = x2, x1
    if y2 < y1: y1, y2 = y2, y1
    ans = gcd(y2 - y1, x2 - x1) + 1 if x1 ^ x2 and y1 ^ y2 else ((y2 - y1) | (x2 - x1)) + 1
    for _ in range(M):
        p = list(minput())
        if not ccw(p, polygon[0], polygon[1]) and x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            ans -= 1
    exit(print(ans))
A = polygon_area_2(polygon) # 2A
B = 0

for i in range(H):
    p1 = polygon[i]
    p2 = polygon[0] if i + 1 == H else polygon[i + 1]
    dx = abs(p2[0] - p1[0])
    dy = abs(p2[1] - p1[1])
    B += gcd(dy, dx) if dy and dx else dx | dy

ans = ((A + B) >> 1) + 1
for _ in range(M):
    p = list(minput())
    ans -= point_in_convex_polygon(p, polygon)

print(ans)
