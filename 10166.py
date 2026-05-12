import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


D1, D2 = minput()
s = set()
for i in range(D1, D2 + 1):
    for j in range(i):
        s.add(Fraction(j, i))

print(len(s))
