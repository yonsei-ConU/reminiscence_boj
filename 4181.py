import sys
from algorithms import convex_hull, angle_sort
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
points = []
for i in range(n):
    p = input_().split()
    if p[2] == 'Y':
        points.append([int(p[0]), int(p[1])])

min_pt = min(points)
hull = convex_hull(points)
x, y = hull[0]
ccw = lambda p1, p2, p3: p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1]
cx = cy = 0
for x, y in hull:
    cx += x
    cy += y

cx /= len(hull)
cy /= len(hull)

sorted_points = deque(angle_sort(points, [cx, cy]))

while sorted_points[0] != min_pt:
    sorted_points.rotate(1)

print(len(sorted_points))
for x, y in sorted_points:
    print(x, y)
