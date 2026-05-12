import sys
from math import asin, sqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


PI = 3.14159265358979323846264338
x1, y1, r1, x2, y2, r2 = map(float, input_().split())
d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if d >= r1 + r2:
    ans = 0
elif abs(r1 - r2) >= d:
    ans = (min(r1, r2) ** 2) * PI
else:
    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = sqrt(r1 ** 2 - a ** 2)
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d
    P1x = x3 + h * (y2 - y1) / d
    P1y = y3 - h * (x2 - x1) / d
    P2x = x3 - h * (y2 - y1) / d
    P2y = y3 + h * (x2 - x1) / d
    dp = sqrt((P1x - P2x) ** 2 + (P1y - P2y) ** 2)
    sin1 = dp / (2 * r1)
    theta1 = asin(sin1)
    sin2 = dp / (2 * r2)
    theta2 = asin(sin2)
    ans = r1 * r1 / 2 * (theta1 - sin1) + r2 * r2 / 2 * (theta2 - sin2)

print(f"{ans:.3f}")
