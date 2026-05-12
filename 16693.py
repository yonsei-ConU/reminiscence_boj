import sys
from math import pi
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


a1, p1 = minput()
r1, p2 = minput()
slice_ = a1 / p1
whole = pi * r1 * r1 / p2
if slice_ > whole:
    print('Slice of pizza')
else:
    print('Whole pizza')
