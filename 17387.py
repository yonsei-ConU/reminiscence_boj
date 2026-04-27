import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


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


x1, y1, x2, y2 = minput()
x3, y3, x4, y4 = minput()
print(+(line_segment_intersection([x1, y1], [x2, y2], [x3, y3], [x4, y4])))

