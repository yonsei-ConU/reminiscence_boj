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


k, n = minput()
g = [[] for _ in range(k << 1)]
for _ in range(n):
    x = input_().split()
    clauses = []
    for i in range(0, 6, 2):
        clauses.append(int(x[i]) - 1 + k * (x[i + 1] == 'R'))
    for piv in range(3):
        for i in range(3):
            if i == piv:
                continue
            g[(clauses[piv] + k) % (2 * k)].append(clauses[i])

scc = getSCC(g)
scc_rev = [0] * (k << 1)
for i in range(len(scc)):
    for c in scc[i]:
        scc_rev[c] = i
for i in range(k):
    if scc_rev[i] == scc_rev[i + k]:
        exit(print(-1))
ans = [-1] * k
for component in scc:
    for c in component:
        idx = c if c < k else c - k
        if ans[idx] == -1:
            ans[idx] = 'RB'[c < k]
print(''.join(ans))
