import sys
from random import shuffle
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def ccw_sign(x1, y1, x2, y2, x3, y3):
    r = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if not r:
        return 0
    elif r > 0:
        return 1
    else:
        return -1


n = int(input_())
p = int(input_())
if n * p <= 200:
    exit(print('possible'))
points = [list(minput()) for _ in range(n)]
MAGIC_NUMBER = 1000

for i in range(MAGIC_NUMBER):
    shuffle(points)
    x1, y1 = points[0]
    x2, y2 = points[1]
    if ccw_sign(x1, y1, x2, y2, points[2][0], points[2][1]):
        continue
    cnt = 3
    for j in range(3, n):
        if not ccw_sign(x1, y1, x2, y2, points[j][0], points[j][1]):
            cnt += 1
    if n * p <= cnt * 100:
        exit(print('possible'))

print('impossible')
