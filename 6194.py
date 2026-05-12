import sys
from math import sqrt
from algorithms import convex_hull
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
points = [tuple(minput()) for _ in range(N)]
hull = convex_hull(points)
perimeter = 0
N = len(hull)
for i in range(N - 1):
    perimeter += sqrt((hull[i][0] - hull[i + 1][0]) ** 2 + (hull[i][1] - hull[i + 1][1]) ** 2)
perimeter += sqrt((hull[N - 1][0] - hull[0][0]) ** 2 + (hull[N - 1][1] - hull[0][1]) ** 2)
print(f"{perimeter:.2f}")
