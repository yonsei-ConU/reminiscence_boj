import sys
from fractions import Fraction
from bisect import bisect_right as upper_bound
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class Line:
    def __init__(self, p, q, idx, x):
        self.p = p
        self.q = q
        self.idx = idx
        self.x = x

    def __repr__(self):
        return f"Line y = {self.p}x + {self.q}, idx {self.idx}, top from {self.x}"


class CHT:
    # 기울기 비증가, 최솟값 ver.
    def __init__(self):
        self.stack = []
        self.inf = 9223372036854775807

    def add(self, p, q, idx):
        if not self.stack:
            self.stack.append(Line(p, q, idx, -self.inf))
        else:
            while True:
                top = self.stack[-1]
                if p == top.p:
                    if top.q < q:
                        self.stack.pop()
                        continue
                    else:
                        break
                intersection = Fraction(q - top.q, top.p - p)
                if intersection <= top.x:
                    self.stack.pop()
                else:
                    self.stack.append(Line(p, q, idx, intersection))
                    break

    def query(self, x):
        lo = -1
        hi = len(self.stack)
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if self.stack[mid].x <= x:
                lo = mid
            else:
                hi = mid
        return self.stack[lo].idx


maxY, minY = minput()
maxY *= 1000
minY *= 1000
n = int(input_())
segments = []
for i in range(n):
    upperX, lowerX = minput()
    segments.append((-upperX, -lowerX, i + 1))

segments.sort(key=lambda x: x[0] - x[1])
cht = CHT()
for u, l, idx in segments:
    cht.add(Fraction(u - l, maxY - minY), Fraction(l, 1) - Fraction(minY * (u - l), maxY - minY), idx)

for _ in range(int(input_())):
    data = input_().rstrip().split('.')
    num = int(data[0]) * 1000
    if '-' not in data[0]:
        num += int(f"{data[1]:0<3}")
    else:
        num -= int(f"{data[1]:0<3}")
    print(cht.query(num))
