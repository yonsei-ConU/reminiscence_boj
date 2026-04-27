import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
q = deque(range(N))
balloons = list(minput())
while q:
    cur = q.popleft()
    print(cur + 1, end=' ')
    v = balloons[cur]
    if v > 0:
        q.rotate(-v + 1)
    else:
        q.rotate(-v)
