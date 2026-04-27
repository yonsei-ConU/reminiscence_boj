import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def graham_scan(points):
    from math import atan2
    if len(points) <= 3: return points

    ccw = lambda p1, p2, p3: p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]
    dist2 = lambda p1, p2: (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

    p0 = min(points, key=lambda p: (p[1], p[0]))
    points = sorted(points, key=lambda p: (atan2(p[1] - p0[1], p[0] - p0[0]), dist2(p, p0)))
    points = [p0] + [p for p in points if p != p0]

    stack = []
    for pt in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], pt) <= 0:
            stack.pop()
        stack.append(pt)
    return stack


N = int(input_())
points = [list(minput()) for _ in range(N)]
print(len(graham_scan(points)))
