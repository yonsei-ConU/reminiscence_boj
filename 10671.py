import sys
from types import GeneratorType
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


def getSCC(g):
    v = len(g)
    disc = [-1] * v
    low = [-1] * v
    stack = []
    in_stack = [False] * v
    t = 0
    ret = []

    @bootstrap
    def dfs(cur):
        nonlocal t
        disc[cur] = t
        low[cur] = t
        t += 1
        stack.append(cur)
        in_stack[cur] = True

        for nxt in g[cur]:
            if disc[nxt] == -1:
                yield dfs(nxt)
                low[cur] = min(low[cur], low[nxt])
            elif in_stack[nxt]:
                low[cur] = min(low[cur], disc[nxt])

        if disc[cur] == low[cur]:
            scc = []
            while 1:
                node = stack.pop()
                scc.append(node)
                in_stack[node] = False
                if cur == node:
                    break
            ret.append(scc)
        yield

    for i in range(v):
        if disc[i] == -1:
            dfs(i)

    return ret


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    X, Y = minput()
    g[X - 1].append(Y - 1)

scc = getSCC(g)[::-1]
scc_rev = [-1] * N
for i in range(len(scc)):
    for v in scc[i]:
        scc_rev[v] = i

transition = [set() for _ in range(len(scc))]
for c in range(N):
    cur = scc_rev[c]
    for n in g[c]:
        nxt = scc_rev[n]
        if cur != nxt:
            assert cur < nxt
            transition[cur].add(nxt)
            transition[nxt].add(cur)

card = [len(c) for c in scc]
dp = [[0, 0]] * len(scc)
dp[0][0] = card[0]
for i in range(1, N):
    
