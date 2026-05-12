import sys
from algorithms import *
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    N = int(input_())
    if not N:
        break
    points = []
    first_point = (-20000, -20000)
    x = y = 0
    for _ in range(N):
        tx, ty = minput()
        x += tx
        y += ty
        points.append((tx, ty))
        if first_point == (-20000, -20000):
            first_point = (tx, ty)
    x /= N
    y /= N
    print(x, y)
    sorted_points = deque(angle_sort(points, (x, y))[::-1])
    while sorted_points[-1] != first_point:
        sorted_points.rotate(1)
    sorted_points.appendleft(first_point)
    print(sorted_points)
    ans = []
    cx, cy = first_point
    for i in range(1, N + 1):
        nx, ny = sorted_points[i]
        if cy > ny:
            ans.append("S")
        elif cy < ny:
            ans.append("N")
        elif cx > nx:
            ans.append("W")
        else:
            assert cx < nx
            ans.append("E")
        cx, cy = nx, ny
    print(''.join(ans))
    input_()
