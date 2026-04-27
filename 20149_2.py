import sys
input_ = sys.stdin.readline
def minput(): return map(Decimal, input_().split())
from decimal import *
getcontext().prec = 50


def line_segment_intersection(p):
    """
    :param: p: [a, b, c, d]
    each element: [x, y]
    :return: whether line segments ab, cd intersects each other.
    """
    v = [0, 0, 0, 0]
    cross_lst = [[0, 2], [0, 3], [1, 2], [1, 3], [2, 0], [2, 1], [3, 0], [3, 1]]
    for i in range(4):
        p1 = [p[cross_lst[2*i][0]][j] - p[cross_lst[2*i][1]][j] for j in [0, 1]]
        p2 = [p[cross_lst[2*i+1][0]][j] - p[cross_lst[2*i+1][1]][j] for j in [0, 1]]
        v[i] = p1[0] * p2[1] - p2[0] * p1[1]
    if sum(vv ** 2 for vv in v) == 0:
        for i in range(2):
            if min(p[2][i], p[3][i]) <= max(p[0][i], p[1][i]) and min(p[0][i], p[1][i]) <= max(p[2][i], p[3][i]) and len(set(p[j][i] for j in range(4))) > 1:
                return -1
        else:
            return 0
    else:
        return +(v[0] * v[1] <= 0 and v[2] * v[3] <= 0)

p = []
a, b, c, d = minput()
p.append([a, b])
p.append([c, d])
a, b, c, d = minput()
p.append([a, b])
p.append([c, d])
res = line_segment_intersection(p)
print(abs(res))
x0, y0 = p[0]
x1, y1 = p[1]
x2, y2 = p[2]
x3, y3 = p[3]
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
