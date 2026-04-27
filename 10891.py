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


def bcc(g):
    v = len(g)
    disc = [-1] * v
    low = [-1] * v
    t = 0
    stack = []
    ret = []

    @bootstrap
    def dfs(cur, parent):
        nonlocal t
        disc[cur] = t
        low[cur] = t
        t += 1
        children_count = 0
        for nxt in g[cur]:
            if disc[nxt] == -1:
                children_count += 1
                stack.append((cur, nxt))
                yield dfs(nxt, cur)
                low[cur] = min(low[cur], low[nxt])
                if parent == -1 and children_count > 1 or parent != -1 and low[nxt] >= disc[cur]:
                    w = None
                    cur_bcc = []
                    while w != (cur, nxt):
                        w = stack.pop()
                        cur_bcc.append(w)
                    ret.append(cur_bcc)
            elif nxt != parent and disc[nxt] < disc[cur]:
                low[cur] = min(low[cur], disc[nxt])
                stack.append((cur, nxt))
        yield

    for root in range(v):
        if disc[root] == -1:
            dfs(root, -1)
            cur_bcc = []
            while stack:
                cur_bcc.append(stack.pop())
            if cur_bcc:
                ret.append(cur_bcc)

    return ret


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    x, y = minput()
    x -= 1; y -= 1
    g[x].append(y)
    g[y].append(x)

BCC = bcc(g)
in_cycle = [False] * N
for comp in BCC:
    vertices = set()
    for u, v in comp:
        vertices.add(u)
        vertices.add(v)
    if len(vertices) == 2 and len(comp) == 1:
        continue
    elif len(vertices) == len(comp):
        for v in vertices:
            if in_cycle[v]:
                exit(print("Not cactus"))
            in_cycle[v] = True
    else:
        exit(print("Not cactus"))

print("Cactus")
