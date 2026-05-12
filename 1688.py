import sys
from algorithms import point_in_non_convex_polygon
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
polygon = [list(minput()) for _ in range(N)]

for _ in range(3):
    p = list(minput())
    print(+point_in_non_convex_polygon(p, polygon))
