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


def kruskal(v, edges):
    mst = set()
    mst_weight = 0
    uf = UnionFind(v+1)
    for fixed_edge in edges[1]:
        weight, s, e = fixed_edge
        if uf.find(s) == uf.find(e):
            assert 0
        else:
            mst.add(fixed_edge)
            mst_weight += weight
            uf.union(s, e)
    edges[0].sort()
    for edge in edges[0]:
        weight, s, e = edge
        if uf.find(s) == uf.find(e):
            continue
        else:
            mst.add(edge)
            mst_weight += weight
            uf.union(s, e)
    return mst_weight


N, M = minput()
edges = [[], []]
total_weight = 0
for _ in range(M):
    a, b, c, d = minput()
    edges[d].append((-c, a, b))
    total_weight += c

w = kruskal(N, edges)
print(total_weight + w)
