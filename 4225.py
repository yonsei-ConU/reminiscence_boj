import sys
from math import sqrt, ceil
from algorithms import convex_hull
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dist_point_line(p, line):
    x0, y0 = p
    (x1, y1), (x2, y2) = line
    return abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) / sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


tc = 1
while True:
    n = int(input_())
    if not n:
        break
    polygon = convex_hull([list(minput()) for _ in range(n)])
    N = len(polygon)
    ans = float('inf')
    for i in range(N):
        p1 = polygon[i]
        p2 = polygon[i + 1] if i + 1 ^ N else polygon[0]
        tmp = 0
        for point in polygon:
            if point != p1 and point != p2:
                tmp = max(tmp, dist_point_line(point, [p1, p2]))
        ans = min(ans, tmp)
    print(f"Case {tc}: {ceil(ans * 100 - 0.0000001)/100:.2f}")
    tc += 1
