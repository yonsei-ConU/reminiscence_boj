import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LCA_preprocess(g, root):
    v = len(g)
    D = [0] * v
    d = [0] * v
    U = [-1] * v
    table = [[0] * v for _ in range(v.bit_length())]

    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        for nxt, weight in g[cur]:
            if nxt == parent:
                continue
            D[nxt] = D[cur] + weight
            d[nxt] = d[cur] + 1
            U[nxt] = cur
            LCA_dfs(nxt, cur)

    LCA_dfs(root, -1)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]

    return D, d, U, table


def LCA_query(u, v):
    """table from precompute must be computed before call"""
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


N = int(input_())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = minput()
    a -= 1; b -= 1
    g[a].append((b, 1)); g[b].append((a, 1))

D, d, U, table = LCA_preprocess(g, 0)

for _ in range(int(input_())):
    u, v = minput()
    u -= 1; v -= 1
    print(LCA_query(u, v) + 1)
