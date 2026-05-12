import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
dist = [-1] * 100001
dist[N] = 0
last = [None] * 100001
q = deque([N])
while q:
    cur = q.popleft()
    for nxt in [cur - 1, cur + 1, cur << 1]:
        if 0 <= nxt <= 100000 and dist[nxt] == -1:
            q.append(nxt)
            dist[nxt] = dist[cur] + 1
            last[nxt] = cur

print(dist[K])
trace = [K]
cur = K
while cur != N:
    cur = last[cur]
    trace.append(cur)

print(*trace[::-1])
