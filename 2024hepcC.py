import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, K = minput()
print(K // (2 ** (N - 1)))
