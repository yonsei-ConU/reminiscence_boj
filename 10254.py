import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def farthest_point(points):
    from functools import cmp_to_key
    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def dist2(p1, p2):
        return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

    def comp(p1, p2):
        x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
        x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
        cross = x1 * y2 - y1 * x2
        if cross > 0:
            return -1
        elif cross < 0:
            return 1
        else:
            d1 = dist2(p1, p0)
            d2 = dist2(p2, p0)
            return -1 if d1 < d2 else 1 if d1 > d2 else 0

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
    points = sorted(points, key=cmp_to_key(lambda p1, p2: comp(p1, p2)))
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
        while True:
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


for _ in range(int(input_())):
    n = int(input_())
    cities = [list(minput()) for _ in range(n)]
    __, p1, p2 = farthest_point(cities)
    print(*p1, *p2)
