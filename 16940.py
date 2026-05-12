import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


N = int(input_())
g = [set() for _ in range(N)]
for _ in range(N - 1):
    a, b = list(minput())
    g[a].add(b)
    g[b].add(a)

query = list(minput())
assert query[0] == 0
q = deque([query[0]])
ptr = 1
visited = [False] * N

while q:
    cur = q.popleft()
    while ptr < N:
        if query[ptr] in g[cur]:
            q.append(query[ptr])
            visited[query[ptr]] = True
            ptr += 1
        else:
            break

print(+(ptr == N))
