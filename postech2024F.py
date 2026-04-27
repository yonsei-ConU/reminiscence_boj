import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

X, M = minput()
print(X * (M + 1))
