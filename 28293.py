import sys
from decimal import *
input_ = sys.stdin.readline
def minput(): return map(Decimal, input_().split())


getcontext().prec = 1000
a, b = minput()
a = a.ln()
res = a * b
res /= Decimal(10).ln()
print(int(res) + 1)
