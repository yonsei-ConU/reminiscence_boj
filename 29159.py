import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


x1 = 0
y1 = 0
for i in range(4):
    x, y = minput()
    x1 += x
    y1 += y

x2 = 0
y2 = 0
for i in range(4):
    x, y = minput()
    x2 += x
    y2 += y

x1 = Fraction(x1, 4)
y1 = Fraction(y1, 4)
x2 = Fraction(x2, 4)
y2 = Fraction(y2, 4)
incl = Fraction(y2 - y1, x2 - x1)
# y1 = incl * x1 + b
b = y1 - incl * x1
print(incl, b)
