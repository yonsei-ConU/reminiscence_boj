import io, os, sys
from array import array
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


def LCA_preprocess(g, root):
    v = len(g)
    D = array('Q', [0] * v)
    d = array('Q', [0] * v)
    table = [array('Q', [0] * v) for _ in range(v.bit_length())]

    @bootstrap
    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        for nxt, weight in g[cur]:
            if nxt == parent:
                continue
            D[nxt] = D[cur] + weight
            d[nxt] = d[cur] + 1
            yield LCA_dfs(nxt, cur)
        yield

    LCA_dfs(root, 0)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]

    return D, d, table


def LCA_query(u, v, d, table):
    if d[v] > d[u]:
        u, v = v, u
    x = d[u] - d[v]
    for i in range(x.bit_length()):
        if x & 1:
            u = table[i][u]
        x >>= 1
    if u == v:
        return u
    for j in range(len(table) - 1, -1, -1):
        if table[j][u] != table[j][v]:
            u = table[j][u]
            v = table[j][v]
    return table[0][v]


N, Q = minput()
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, w = minput()
    a -= 1; b -= 1
    g[a].append((b, w)); g[b].append((a, w))

D, d, table = LCA_preprocess(g, 0)

for q in range(Q):
    u, v = minput()
    u -= 1; v -= 1
    lca = LCA_query(u, v, d, table)
    sys.stdout.write(str(D[u] + D[v] - 2 * D[lca]))
    if q != Q - 1:
        sys.stdout.write('\n')

os._exit(0)
