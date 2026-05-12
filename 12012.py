import sys
from algorithms import UnionFind
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(M):
    u, v = minput()
    u -= 1; v -= 1
    g[u].append(v)
    g[v].append(u)

queries = [int(input_()) - 1 for _ in range(N)][::-1]
ans = []
opened = [False] * N
uf = UnionFind(N)
for i in range(N):
    q = queries[i]
    opened[q] = True
    for v in g[q]:
        if opened[v]:
            uf.union(v, q)
    if uf.size[uf.find(q)] == i + 1:
        ans.append("YES")
    else:
        ans.append("NO")

print('\n'.join(ans[::-1]))
