import sys
input_ = sys.stdin.readline
def minput(): return map(Decimal, input_().split())
from decimal import *
getcontext().prec = 50


def ccw(a, b, c):
    cross_product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0

def line_segment_intersection(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if ab == 0 and cd == 0:
        a, b = sorted([a, b])
        c, d = sorted([c, d])
        return not (b < c or d < a)
    
    return ab <= 0 and cd <= 0


a, b, c, d = minput()
A = [a, b]
B = [c, d]
a, b, c, d = minput()
C = [a, b]
D = [c, d]
res = line_segment_intersection(A, B, C, D)
print(abs(res))
x0, y0 = A
x1, y1 = B
x2, y2 = C
x3, y3 = D
if res == 1:
    x = ((x0 * y1 - x1 * y0) * (x2 - x3) + (x2 * y3 - x3 * y2) * (x1 - x0)) / ((y1 - y0) * (x2 - x3) + (x1 - x0) * (y3 - y2))
    y = ((x0 * y1 - x1 * y0) * (y3 - y2) - (x2 * y3 - x3 * y2) * (y1 - y0)) / ((y1 - y0) * (x3 - x2) + (x0 - x1) * (y3 - y2))
    print(x, y)
elif res == -1:
    if min(x2, x3) == max(x0, x1) and not (x0 == x1 == x2 == x3):
        if max(x0, x1) == x0:
            print(x0, y0)
        else:
            print(x1, y1)
    elif min(y2, y3) == max(y0, y1) and not (y0 == y1 == y2 == y3):
        if max(y0, y1) == y0:
            print(x0, y0)
        else:
            print(x1, y1)
    elif min(x0, x1) == max(x2, x3) and not (x0 == x1 == x2 == x3):
        if min(x0, x1) == x0:
            print(x0, y0)
        else:
            print(x1, y1)
    elif min(y0, y1) == max(y2, y3) and not (y0 == y1 == y2 == y3):
        if min(y0, y1) == y0:
            print(x0, y0)
        else:
            print(x1, y1)
