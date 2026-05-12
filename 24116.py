import sys
from algorithms import UnionFind
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def kruskal(v, edges):
    if N == K:
        return 0
    edges.sort()
    uf = UnionFind(v)
    ret = cnt = 0
    for edge in edges:
        weight, s, e = edge
        if uf.find(s) != uf.find(e):
            ret += weight
            cnt += 1
            uf.union(s, e)
            if cnt == N - K:
                return ret
    assert False


N, M, K = minput()
edges = []
for _ in range(M):
    A, B, C = minput()
    edges.append((C, A - 1, B - 1))

print(kruskal(N, edges))
