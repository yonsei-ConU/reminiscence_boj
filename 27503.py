import sys
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


def two_sat(N, trace=False):
    scc = getSCC(g)
    scc_rev = [0] * (N << 1)
    for i in range(len(scc)):
        for c in scc[i]:
            scc_rev[c] = i
    for i in range(N):
        if scc_rev[i] == scc_rev[i + N]:
            return 0
    if not trace:
        return 1
    ret = [-1] * N
    for component in scc:
        for c in component:
            idx = c if c < N else c - N
            if ret[idx] == -1:
                ret[idx] = c < N
    return ret


N, M, C, K = minput()
A = list(minput())
g = [[] for _ in range(2 * N)]
replaceable = set()
for _ in range(C):
    u, v = minput(); u -= 1; v -= 1
    replaceable.add(u)
    replaceable.add(v)
    g[v + N].append(u)
    g[u + N].append(v)
for v in A:
    v -= 1
    if v not in replaceable:
        g[v + N].append(v)
for _ in range(K):
    a, b = minput(); a -= 1; b -= 1
    g[a].append(b + N)
    g[b].append(a + N)
if two_sat(N):
    print("YES")
else:
    print("NO")
