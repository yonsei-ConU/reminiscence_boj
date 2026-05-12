import sys
from math import sin, cos, pi
from algorithms import line_segment_intersection
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
segments = []
for _ in range(n):
    pp = list(minput())
    t = []
    for p in pp:
        t.append([1000 * cos(pi * p / 1800), 1000 * sin(pi * p / 1800)])
    segments.append(t)

theta, r = minput()
rlwns1 = [r * cos(pi * theta / 1800), r * sin(pi * theta / 1800)]
theta, r = minput()
rlwns2 = [r * cos(pi * theta / 1800), r * sin(pi * theta / 1800)]

ans = 0
for i in range(n):
    ans += line_segment_intersection(segments[i][0], segments[i][1], rlwns1, rlwns2)

print('YNEOS'[ans & 1::2])
