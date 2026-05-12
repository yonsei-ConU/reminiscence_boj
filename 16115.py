import sys
from math import atan2, pi
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
max_dist = -1
farthest = []

for _ in range(N):
    x, y = minput()
    if x ** 2 + y ** 2 == max_dist:
        farthest.append(atan2(y, x))
    elif x ** 2 + y ** 2 > max_dist:
        max_dist = x ** 2 + y ** 2
        farthest = [atan2(y, x)]
farthest.append(farthest[0])

ans = 0
for i in range(len(farthest) - 1):
    p1, p2 = farthest[i], farthest[i + 1]
    diff = p2 - p1
    if not diff:
        diff = 2 * pi
    elif p1 > p2:
        diff += 2 * pi
    if diff > ans:
        ans = diff

print(ans * 180 / pi)
