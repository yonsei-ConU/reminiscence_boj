import sys
from math import tan, atan, pi
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


k, w, l = minput()
lo = 0
hi = pi / 2

for i in range(35):
    mid = (lo + hi) / 2
    x = w / 2
    y = 0
    theta = mid
    bounce = 0
    direction = -1

    while y < l:
        new_x = 0 if direction == -1 else w
        if abs(x - new_x) * tan(theta) > l - y:
            x += direction / tan(theta) * (l - y)
            y = l
        else:
            y += abs(new_x - x) * tan(theta)
            x = new_x
            bounce += 1
            if bounce > k:
                break
            theta = atan(2 * tan(theta))
            direction *= -1

    if bounce > k or (bounce == k and ((bounce % 2 and x > w / 2) or (not bounce % 2 and x < w / 2))):
        lo = mid
    else:
        hi = mid

print(f"{mid * 180 / pi:.12f}")
