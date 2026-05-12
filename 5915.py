import sys
from collections import defaultdict
from algorithms import UnionFind
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def kruskal(v, edges):
    edges.sort()
    uf = UnionFind(v)
    mst_weight = 0
    edge_weights = defaultdict(int)
    for edge in edges:
        weight, s, e = edge
        if uf.find(s) != uf.find(e):
            mst_weight += weight
            uf.union(s, e)
            edge_weights[weight] += 1
    return mst_weight, edge_weights


N, M = minput()
edges = []
edges_by_weight = defaultdict(list)
weight_count = defaultdict(int)
for i in range(M):
    a, b, n = minput()
    edges.append((n, a - 1, b - 1))
    edges_by_weight[n].append((a - 1, b - 1))
    weight_count[n] += 1

mst_weight, edge_weights = kruskal(N, edges)
MOD = 10 ** 9 + 7
ans = 1
uf = UnionFind(N)
for w in sorted(edge_weights):
    if edge_weights[w] == weight_count[w]:
        for s, e in edges_by_weight[w]:
            uf.union(s, e)
    else:
        s = set()
        for u, v in edges_by_weight[w]:
            s.add(uf.find(u))
            s.add(uf.find(v))
        mult = 0
        for mask in range(1 << len(edges_by_weight[w])):
            if mask.bit_count() != edge_weights[w]:
                continue
            t = set()
            for i in range(len(edges_by_weight[w])):
                if mask & (1 << i):
                    u, v = edges_by_weight[w][i]
                    t.add(uf.find(u))
                    t.add(uf.find(v))
            if len(s) == len(t):
                mult += 1
        ans = (ans * mult) % MOD
        for u, v in edges_by_weight[w]:
            uf.union(u, v)

print(mst_weight, ans)
