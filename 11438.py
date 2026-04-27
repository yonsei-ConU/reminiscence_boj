import sys
sys.setrecursionlimit(100000)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LCA_pre_dfs(g, cur, parent):
    """
    predefine
    D := [0] * len(g)
    U := [-1] * len(g), 0 for root
    before function call
    """
    for nxt, weight in g[cur]:
        if nxt == parent:
            continue
        D[nxt] = D[cur] + weight
        U[nxt] = cur
        LCA_pre_dfs(g, nxt, cur)


def LCA_precompute(g, U):
    """U from pre_dfs must be computed before call"""
    v = len(g)
    table = [[0] * v for _ in range(v.bit_length())]
    table[0] = U[:]
    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i - 1][table[i - 1][j]]
    return table


def LCA_query(u, v):
    """table from precompute must be computed before call"""
    if D[v] > D[u]:
        u, v = v, u
    x = D[u] - D[v]
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

D = [0] * N
U = [-1] * N
U[0] = 0
LCA_pre_dfs(g, 0, -1)
table = LCA_precompute(g, U)

for _ in range(int(input_())):
    u, v = minput()
    u -= 1; v -= 1
    print(LCA_query(u, v) + 1)
