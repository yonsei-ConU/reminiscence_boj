import sys
from itertools import combinations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def polygon_area(points):
    area = 0
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        area += p1[0] * p2[1] - p1[1] * p2[0]
    return abs(area)


N = int(input_())
points = [list(minput()) for _ in range(N)]
ans = 0
for p in combinations(points, 3):
    x = {a[0] for a in p}
    y = {a[1] for a in p}
    if len(x) == len(y) == 2: ans = max(ans, polygon_area(p))

print(ans)
