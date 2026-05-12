import io, os, sys
from collections import deque
sys.setrecursionlimit(10001)
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def dfs(cur, parent):
    sz[cur] = 1
    for nxt in g[cur]:
        if nxt == parent:
            continue
        weight = g[cur][nxt]
        par[nxt] = cur
        dfs(nxt, cur)
        sz[cur] += sz[nxt]
        cost[cur] += sz[nxt] * weight + cost[nxt]


output = []
while 1:
    n = int(input_())
    if not n:
        break
    g = [{} for _ in range(n)]
    for __ in range(n - 1):
        a, b, w = minput()
        g[a][b] = w
        g[b][a] = w
    sz = [0] * n
    cost = [0] * n
    par = [0] * n
    dfs(0, 0)
    q = deque([0])
    ans = [float('inf')] * n
    ans[0] = cost[0]
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if nxt == par[cur]:
                continue
            ans[nxt] = ans[cur] + g[cur][nxt] * (n - 2 * sz[nxt])
            q.append(nxt)
    output.append(str(min(ans)))
os.write(1, '\n'.join(output).encode())
os._exit(0)
