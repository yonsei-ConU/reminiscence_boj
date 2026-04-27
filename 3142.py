import sys
from math import gcd, isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def print_(a): sys.stdout.write(str(a) + '\n')


N = int(input_())
t = 1

for _ in range(N):
    a = int(input_())
    t = t * a // gcd(a, t) ** 2
    if isqrt(t) ** 2 == t:
        t = 1
    if t == 1:
        print_('DA')
    else:
        print_('NE')
