import sys
from types import GeneratorType
from collections import deque
input_ = sys.stdin.readline
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
    for nxt in g[cur]:
        if nxt == parent:
            continue
        yield dfs(nxt, cur)
        sz[cur] += sz[nxt]
        dp[cur] += sz[nxt] * g[cur][nxt] + dp[nxt]
    yield


N = int(input_())
data = [input_().split() for _ in range(N)]
g = [{} for _ in range(N)]
par = [0] * N
sz = [0] * N  # i번을 루트로 하는 서브트리에서 리프노드의 개수
leaf = 0
for i in range(N):
    child = tuple(map(int, data[i][2:]))
    if not child:
        sz[i] = 1
        leaf += 1
    for c in child:
        c -= 1
        par[c] = i
        if int(data[c][1]):
            g[i][c] = len(data[c][0]) + 1
            g[c][i] = 3
        else:
            g[i][c] = len(data[c][0])

# dp[i] = i번 ~ 리프 거리의 합 for all leaf
dp = [0] * N
dfs(0, 0)
ans = [10 ** 12] * N
ans[0] = dp[0]
q = deque([0])
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if len(data[nxt]) <= 2 or ans[nxt] != 10 ** 12:
            continue
        ans[nxt] = ans[cur] - g[cur][nxt] * sz[nxt] + g[nxt][cur] * (leaf - sz[nxt])
        q.append(nxt)

print(min(ans))
