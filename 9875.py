import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def convex_hull(points):
    if len(points) <= 3: return points
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


def point_in_convex_polygon(p, polygon):
    """
    assuming that polygon is ccw
    """
    ccw = lambda p1, p2, p3: p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]
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
            if (p[0] - rlwns[0]) ** 2 + (p[1] - rlwns[1]) ** 2 <= (polygon[mid][0] - rlwns[0]) ** 2 + (polygon[mid][1] - rlwns[1]) ** 2:
                return True
            else:
                return False
    if not lo or hi == len(polygon):
        return False
    return ccw(polygon[lo], polygon[hi], p) >= 0  # >0 for strictly inside, >=0 for inside and boundary


N = int(input_())
A = [list(minput()) for _ in range(N)]
B = [list(minput()) for _ in range(N)]
A_hull = convex_hull(A)
B_hull = convex_hull(B)
A_score = sum(point_in_convex_polygon(p, A_hull) for p in B)
B_score = sum(point_in_convex_polygon(p, B_hull) for p in A)

print(A_score, B_score)
