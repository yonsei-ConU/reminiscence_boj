import sys
sys.setrecursionlimit(100001)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def get_sparse_table(g, root):
    g[root][root] = 0
    v = len(g)
    d = [0] * v
    table = [[0] * v for _ in range(v.bit_length())]
    max_table = [[0] * v for _ in range(v.bit_length())]
    min_table = [[0] * v for _ in range(v.bit_length())]

    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        if cur != parent:
            max_table[0][cur] = g[cur][parent]
            min_table[0][cur] = g[cur][parent]
        for nxt in g[cur]:
            if nxt == parent:
                continue
            d[nxt] = d[cur] + 1
            LCA_dfs(nxt, cur)

    LCA_dfs(root, root)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]
            max_table[i][j] = max(max_table[i - 1][j], max_table[i - 1][table[i - 1][j]])
            min_table[i][j] = min(min_table[i - 1][j], min_table[i - 1][table[i - 1][j]])

    return d, table, max_table, min_table


def path_minmax(u, v):
    if u == v:
        return 0, 0
    if d[v] > d[u]:
        u, v = v, u
    x = d[u] - d[v]
    RET = -float('inf')
    ret = float('inf')
    for i in range(x.bit_length()):
        if x & 1:
            RET = max(RET, max_table[i][u])
            ret = min(ret, min_table[i][u])
            u = table[i][u]
        x >>= 1
    if u == v:
        return ret, RET
    for j in range(len(table) - 1, -1, -1):
        if table[j][u] != table[j][v]:
            RET = max(RET, max_table[j][u], max_table[j][v])
            ret = min(ret, min_table[j][u], min_table[j][v])
            u = table[j][u]
            v = table[j][v]
    RET = max(RET, max_table[0][u], max_table[0][v])
    ret = min(ret, min_table[0][u], min_table[0][v])
    return ret, RET


N = int(input_())
g = [{} for _ in range(N)]
for _ in range(N - 1):
    A, B, C = minput()
    A -= 1; B -= 1
    g[A][B] = C
    g[B][A] = C

d, table, max_table, min_table = get_sparse_table(g, 0)
for _ in range(int(input_())):
    D, E = minput()
    print(*path_minmax(D - 1, E - 1))
