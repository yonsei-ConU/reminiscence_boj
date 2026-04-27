import io, os, sys
sys.setrecursionlimit(100001)
from collections import deque
from types import GeneratorType
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def dfs(cur, parent):
    sz[cur] = 1
    for nxt, weight in g[cur].items():
        if nxt == parent:
            continue
        par[nxt] = cur
        yield dfs(nxt, cur)
        sz[cur] += sz[nxt]
        cost[cur] += sz[nxt] * weight + cost[nxt]
    yield


output = []
N = int(input_())
g = [{} for _ in range(N)]
for _ in range(N - 1):
    a, b, w = minput()
    a -= 1; b -= 1
    g[a][b] = w
    g[b][a] = w
sz = [0] * N
cost = [0] * N
par = [0] * N
dfs(0, 0)
q = deque([0])
ans = [float('inf')] * N
ans[0] = cost[0]
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if nxt == par[cur]:
            continue
        ans[nxt] = ans[cur] + g[cur][nxt] * (N - 2 * sz[nxt])
        q.append(nxt)

ans1_idx = -1
ans1_val = float('inf')
for i in range(N):
    if ans[i] < ans1_val:
        ans1_idx = i
        ans1_val = ans[i]

M = int(input_())
g = [{} for _ in range(N)]
for _ in range(M - 1):
    a, b, w = minput()
    a -= 1; b -= 1
    g[a][b] = w
    g[b][a] = w
sz = [0] * N
cost = [0] * N
par = [0] * N
dfs(0, 0)
q = deque([0])
ans = [float('inf')] * M
ans[0] = cost[0]
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if nxt == par[cur]:
            continue
        ans[nxt] = ans[cur] + g[cur][nxt] * (M - 2 * sz[nxt])
        q.append(nxt)

ans2_idx = -1
ans2_val = float('inf')
for i in range(M):
    if ans[i] < ans2_val:
        ans2_idx = i
        ans2_val = ans[i]

output.append(f"{ans1_idx + 1} {ans2_idx + 1}")
output.append(str(M * ans1_val + N * ans2_val + M * N))

os.write(1, '\n'.join(output).encode())
os._exit(0)
