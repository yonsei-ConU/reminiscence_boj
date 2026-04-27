import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
if N == 1: exit(print('YES'))
b = list(minput())
if not M or not min(b): exit(print('NO'))
edges = [list(minput()) for _ in range(M)]
