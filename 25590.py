import sys
from algorithms import bootstrap
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LCA_preprocess(g, root):
    v = len(g)
    d = [0] * v
    table = [[0] * v for _ in range(v.bit_length())]

    @bootstrap
    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        for nxt in g[cur]:
            if nxt == parent:
                continue
            d[nxt] = d[cur] + 1
            yield LCA_dfs(nxt, cur)
        yield

    LCA_dfs(root, -1)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]

    return d, table  # depth, table


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


N, M, K, S = minput()
if K < S: exit(print(0))
queries = []
for u in range(N):
    for v in list(minput())[1:]:
        queries.append((u, v - 1))

g = [[] for _ in range(N + S)]
root = [True] * (N + S)
for u in range(N + S):
    lst = list(minput())
    if len(lst) - 1 > M:
        exit(print(0))
    for v in lst[1:]:
        v -= 1
        root[v] = False
        g[u].append(v)
        g[v].append(u)

assert sum(root) == 1
for i in range(N + S):
    if root[i]:
        root = i
        break

d, table = LCA_preprocess(g, root)
for u, v in queries:
    if LCA_query(u, v, d, table) != u:
        exit(print(0))

print(1)
