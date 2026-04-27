import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def kruskal(v, e):
    edges = sorted(e)
    uf = UnionFind(v)
    ret = set()
    mst_weights = []
    for edge in edges:
        weight, s, e = edge
        if uf.find(s) == uf.find(e):
            continue
        else:
            ret.add((weight, min(s, e), max(s, e)))
            uf.union(s, e)
            mst_weights.append(weight)
    roots = set(uf.find(i) for i in range(v))
    if len(roots) != 1:
        exit(print(-1))
    return ret, mst_weights


def get_sparse_table(g, root):
    g[root][root] = -float('inf')
    v = len(g)
    d = [0] * v
    table = [[0] * v for _ in range(v.bit_length())]
    max_table = [[-float('inf')] * v for _ in range(v.bit_length())]

    def LCA_dfs(cur, parent):
        table[0][cur] = parent
        if cur != parent:
            max_table[0][cur] = g[cur][parent]
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

    return d, table, max_table


def path_maximum(u, v):
    if u == v:
        return 0
    if d[v] > d[u]:
        u, v = v, u
    x = d[u] - d[v]
    ret = -float('inf')
    for i in range(x.bit_length()):
        if x & 1:
            ret = max(ret, max_table[i][u])
            u = table[i][u]
        x >>= 1
    if u == v:
        return ret
    for j in range(len(table) - 1, -1, -1):
        if table[j][u] != table[j][v]:
            ret = max(ret, max_table[j][u], max_table[j][v])
            u = table[j][u]
            v = table[j][v]
    ret = max(ret, max_table[0][u], max_table[0][v])
    return ret


V, E = minput()
edges = []
for _ in range(E):
    a, b, weight = minput()
    edges.append((weight, a - 1, b - 1))
mst_edges, mst_weights = kruskal(V, edges)
mst_weight = sum(mst_weights)
mst_edges = set(mst_edges)
mst_weights = sorted(set(mst_weights), reverse=True)
if len(mst_weights) == 1: exit(print(-1))
mst = [{} for _ in range(V)]
for weight, a, b in mst_edges:
    mst[a][b] = weight
    mst[b][a] = weight

d, table, max_table = get_sparse_table(mst, 0)
ans = float('inf')
for weight, start, end in edges:
    if (weight, min(start, end), max(start, end)) in mst_edges:
        print(mst_weight)
        continue
    max_w = path_maximum(start, end)
    print(mst_weight - max_w + weight)
