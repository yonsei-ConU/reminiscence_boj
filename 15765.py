import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LCA_preprocess(g, root):
    v = len(g)
    d = defaultdict(int)
    table = [defaultdict(str) for _ in range(v.bit_length())]

    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        for nxt in g[cur]:
            if nxt == parent:
                continue
            d[nxt] = d[cur] + 1
            LCA_dfs(nxt, cur)

    LCA_dfs(root, -1)

    for i in range(1, v.bit_length()):
        for j in range(v):
            table[i][j] = table[i-1][table[i-1][j]]

    return d, table


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


N, q1, q2 = input_().split()
N = int(N)
g = {}
for i in range(N - 1):
    
