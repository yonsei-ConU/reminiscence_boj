import sys
from algorithms import bootstrap
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


@bootstrap
def dfs(cur, depth, visited):
    global ans
    if depth == 4:
        ans = 1
        yield True
    for nxt in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            v = yield dfs(nxt, depth + 1, visited)
            if v:
                yield True
            visited[nxt] = False
    yield False


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = minput()
    g[a].append(b)
    g[b].append(a)

ans = 0
for start in range(N):
    visited = [False] * N
    visited[start] = True
    dfs(start, 0, visited)

print(ans)
