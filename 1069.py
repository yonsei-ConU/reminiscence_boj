import sys
from math import sqrt, ceil
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X, Y, D, T = minput()
if T > D:
    # print('case 1')
    print(sqrt(X ** 2 + Y ** 2))
elif X ** 2 + Y ** 2 < D ** 2:
    # print('case 2')
    print(min(2 * T, sqrt(X ** 2 + Y ** 2), T + D - sqrt(X ** 2 + Y ** 2)))
else:
    dist = sqrt(X ** 2 + Y ** 2)
    # print('case 3')
    print(min(T * ceil(dist / D), T * int(dist / D) + dist - int(dist / D) * D))
