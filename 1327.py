import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
cur = tuple(minput())
q = deque([cur])
dist = {cur: 0}
sorted_list = tuple(range(1, N + 1))

while q:
    cur = q.popleft()
    if cur == sorted_list:
        exit(print(dist[cur]))
    for idx in range(N - K + 1):
        t = list(cur)
        left = idx
        right = K - 1 + idx
        while left < right:
            t[left], t[right] = t[right], t[left]
            left += 1
            right -= 1
        nxt = tuple(t)
        if nxt not in dist:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(-1)
