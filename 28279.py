import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
q = deque()
for _ in range(N):
    query = list(minput())
    if query[0] == 1:
        q.appendleft(query[1])
    elif query[0] == 2:
        q.append(query[1])
    elif query[0] == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif query[0] == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif query[0] == 5:
        print(len(q))
    elif query[0] == 6:
        print(+(len(q) == 0))
    elif query[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
