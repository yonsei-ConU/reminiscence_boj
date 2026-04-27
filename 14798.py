import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for _ in range(int(input_())):
    R, C = minput()
    cake = [input_().rstrip() for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if cake[i][j] != '?':
