import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def farthest_point(points):
    from math import atan2

    ccw = lambda p1, p2, p3: p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]
    dist2 = lambda p1, p2: (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

    if len(points) == 1:
        return 0, points[0], points[0]

    elif len(points) == 2:
        return dist2(points[0], points[1]), points[0], points[1]

    elif len(points) == 3:
        d1 = dist2(points[0], points[1])
        d2 = dist2(points[0], points[2])
        d3 = dist2(points[1], points[2])
        if d1 >= d2 and d1 >= d3:
            return d1, points[0], points[1]
        elif d2 >= d1 and d2 >= d3:
            return d2, points[0], points[2]
        else:
            return d3, points[1], points[2]

    p0 = min(points, key=lambda p: (p[1], p[0]))
    points = sorted(points, key=lambda p: (atan2(p[1] - p0[1], p[0] - p0[0]), dist2(p, p0)))
    points = [p0] + [p for p in points if p != p0]

    stack = []
    for pt in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], pt) <= 0:
            stack.pop()
        stack.append(pt)

    ans_dist = -1
    ptr1 = 0
    ptr2 = 1
    ans_pt1 = 0
    ans_pt2 = 1

    while ptr1 < len(stack):
        while 1:
            next_ptr2 = (ptr2 + 1) % len(stack)
            cur_dist = dist2(stack[ptr1], stack[ptr2])
            nxt_dist = dist2(stack[ptr1], stack[next_ptr2])
            if nxt_dist > cur_dist:
                ptr2 = next_ptr2
            else:
                break
        if cur_dist > ans_dist:
            ans_dist = cur_dist
            ans_pt1 = ptr1
            ans_pt2 = ptr2
        ptr1 += 1

    return ans_dist, stack[ans_pt1], stack[ans_pt2]


n = int(input_())
cities = list(set(tuple(minput()) for _ in range(n)))
ans, __, __ = farthest_point(cities)
print(ans)
