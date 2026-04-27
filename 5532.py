import sys
from math import ceil
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


L, A, B, C, D = [int(input_()) for _ in '     ']
print(L - max(ceil(A / C), ceil(B / D)))
