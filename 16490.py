import sys
from math import sqrt
input_ = sys.stdin.readline
def mfnput(): return map(float, input_().split())


def solve_quadratic(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return None
    return max((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))


a, t = mfnput()
cos = sqrt(1 - (3 * a * a) / (4 * t * t))
b = solve_quadratic(1, -2 * t * cos, t * t - a * a)
c = solve_quadratic(1, 2 * t * cos, t * t - a * a)
print(round(b * c))
