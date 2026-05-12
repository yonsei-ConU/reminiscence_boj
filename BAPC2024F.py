import sys
from decimal import *
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def bootstrap(f, stack=[]):
    from types import GeneratorType
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


getcontext().prec = 300
n, m = minput()
prob = list(map(lambda x: 1 - Decimal(x), input_().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = minput()
    g[b - 1].append(a - 1)

scc = getSCC(g)[::-1]
scc_rev = [0] * n
for i in range(len(scc)):
    for v in scc[i]:
        scc_rev[v] = i
ans = [Decimal(1)] * len(scc)
for i in range(n):
    ans[scc_rev[i]] *= prob[i]

for i in range(len(scc)):
    nxt = set()
    for u in scc[i]:
        for v in g[u]:
            if scc_rev[v] != i:
                nxt.add(scc_rev[v])
    for v in nxt:
        assert v > i
        ans[v] *= ans[i]

aaaa = max(ans)
a = [str(int(aaaa))] + ['.']
aaaa -= int(aaaa)
for i in range(300):
    aaaa *= 10
    a.append(str(int(aaaa)))
    aaaa -= int(aaaa)

print(''.join(a))
