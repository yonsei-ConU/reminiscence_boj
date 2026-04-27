import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
B = list(minput())
q = deque()
for i in range(N):
    if not A[i]:
        q.append(B[i])

M = int(input_())
for c in list(minput()):
    q.appendleft(c)
    print(q.pop(), end=' ')
