import sys
from math import sqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dist(t):
    return sqrt((Cx - (Ax * t + Bx * (1 - t))) ** 2 + (Cy - (Ay * t + By * (1 - t))) ** 2 + (Cz - (Az * t + Bz * (1 - t))) ** 2)


Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = minput()
lo = 0
hi = 1
for i in range(100):
    left = (2 * lo + hi) / 3
    right = (lo + 2 * hi) / 3
    if dist(left) > dist(right):
        lo = left
    else:
        hi = right

print(f"{dist(lo):.15f}")
