import sys
from algorithms import convex_hull
from math import atan2, pi
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
points = [list(minput()) for _ in range(n)]
hull = convex_hull(points)
# right
angle1 = atan2(hull[1][1] - hull[0][1], hull[0][0] - hull[1][0]) * 180 / pi
# left
angle2 = atan2(hull[-2][1] - hull[-1][1], hull[-2][0] - hull[-1][0]) * 180 / pi
print(max(angle1, angle2))
