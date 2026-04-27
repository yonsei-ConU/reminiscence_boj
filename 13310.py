import sys
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


def rotating_calipers(hull):
    n = len(hull)
    dist2 = lambda p1, p2: (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2
    ccw = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    if n == 1:
        return 0
    elif n == 2:
        return dist2(hull[0], hull[1])
    elif n == 3:
        d1 = dist2(hull[0], hull[1])
        d2 = dist2(hull[0], hull[2])
        d3 = dist2(hull[1], hull[2])
        return max(d1, d2, d3)

    max_dist = 0
    j = 1
    for i in range(n):
        next_i = (i + 1) % n
        while True:
            next_j = (j + 1) % n
            cross = ccw(hull[i], hull[next_i], hull[next_j]) - ccw(hull[i], hull[next_i], hull[j])
            if cross > 0:
                j = next_j
            else:
                break

        current_dist = dist2(hull[i], hull[j])
        if current_dist > max_dist:
            max_dist = current_dist
    return max_dist


N, T = minput()
stars = [tuple(minput()) for _ in range(N)]
get_stars = lambda t: [(x + dx * t, y + dy * t) for x, y, dx, dy in stars]
lo = -1
hi = T + 1
while lo + 2 < hi:
    left = (lo + hi) >> 1
    right = left + 1
    if rotating_calipers(convex_hull(get_stars(left))) > rotating_calipers(convex_hull(get_stars(right))):
        lo = left
    else:
        hi = right

ans_day = -1
ans_val = 99999999999999999
for day in range(max(0, lo), min(hi + 1, T + 1)):
    val = rotating_calipers(convex_hull(get_stars(day)))
    if val < ans_val:
        ans_day = day
        ans_val = val

assert 0 <= ans_day <= T
print(ans_day)
print(ans_val)
