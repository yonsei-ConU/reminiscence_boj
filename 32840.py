import sys
from math import gcd as gcd_
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def gcd(a, b):
    if not a or not b:
        return a | b
    else:
        return gcd_(a, b)


def add_list(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def sub_list(a, b):
    return [a[i] - b[i] for i in range(len(a))]


def polygon_area_2(points):
    area = 0
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        area += p1[0] * p2[1] - p1[1] * p2[0]
    return abs(area)


data = list(minput())
A = [data[0], data[1]]
B = [data[2], data[3]]
C = [data[4], data[5]]

AB = [B[0] - A[0], B[1] - A[1]]
BC = [C[0] - B[0], C[1] - B[1]]
CA = [A[0] - C[0], A[1] - C[1]]

candidates = []
x = gcd(abs(AB[0]), abs(AB[1]))
d = [AB[0] // x, AB[1] // x]
candidates.append([add_list(A, d), sub_list(B, d)])
y = gcd(abs(BC[0]), abs(BC[1]))
d = [BC[0] // y, BC[1] // y]
candidates.append([add_list(B, d), sub_list(C, d)])
z = gcd(abs(CA[0]), abs(CA[1]))
d = [CA[0] // z, CA[1] // z]
candidates.append([add_list(C, d), sub_list(A, d)])
if x == 1 or y == 1 or z == 1:
    exit(print(-1))

areas = []
for mask in range(8):
    points = []
    for i in range(3):
        if mask & (1 << i):
            points.append(candidates[i][1])
        else:
            points.append(candidates[i][0])
    areas.append(polygon_area_2(points))

print(max(areas), min(areas))
