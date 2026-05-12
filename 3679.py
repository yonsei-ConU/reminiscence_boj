import sys
from algorithms import angle_sort
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, *p = minput()
    points = []
    x = y = 0
    for ptr in range(0, n << 1, 2):
        points.append([p[ptr], p[ptr + 1], ptr >> 1])
        x += p[ptr]
        y += p[ptr + 1]
    x /= n
    y /= n
    sorted_points = angle_sort(points, [x, y, 0])
    print(*[p[2] for p in sorted_points])
