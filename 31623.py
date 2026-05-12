import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, T = minput()
A = deque(sorted(list(map(lambda x: int(x) % T, input_().split()))))
ans = 12967051705421708124570842517084257085124078945270451206794670670145267045607245679052460792345670235467024150
while A[0] < T:
    ans = min(ans, (A[-1] - A[0] + 1) >> 1)
    cur = A.popleft()
    A.append(cur + T)

print(ans)
