import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from collections import deque


N, S, P = minput()
P -= 1
g = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = minput()
    g[A-1].append(B-1)
    g[B-1].append(A-1)

q = deque([P])
dist = [0] * (N)
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if not dist[nxt]:
            q.append(nxt)
            dist[nxt] = dist[cur] + 1

jijidae = dist[:S]
jijidae.sort()
print(N - 1 - jijidae[0] - jijidae[1])
