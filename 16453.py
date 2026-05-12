import sys
from algorithms import LCA_preprocess, LCA_query
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


N, Q = minput()
N += 1
Q += 1
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = minput()
    g[u].append(v)
    g[v].append(u)

d, table = LCA_preprocess(g, 0)
for _ in range(Q):
    u1, u2, v1, v2 = minput()
    print([LCA_query(u1, v1, d, table), LCA_query(u1, v2, d, table), LCA_query(u2, v1, d, table), LCA_query(u2, v2, d, table)])
    lca = {LCA_query(u1, v1, d, table), LCA_query(u1, v2, d, table), LCA_query(u2, v1, d, table), LCA_query(u2, v2, d, table)}
    if len(lca) == 1:
        print(0)
    elif len(lca) == 2:
        print(abs(d[lca.pop()] - d[lca.pop()]) + 1)
    elif len(lca) == 3:
        depth = [d[u] for u in lca]
        print(sum(depth) - min(depth) * 3 + 1)
    else:
        assert False
