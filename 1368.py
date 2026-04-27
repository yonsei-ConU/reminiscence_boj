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
    edges.sort()
    uf = UnionFind(v+1)
    mst = set()
    mst_weight = 0
    for edge in edges:
        weight, s, e = edge
        if uf.find(s) == uf.find(e):
            continue
        else:
            mst.add(edge)
            mst_weight += weight
            uf.union(s, e)
    return mst_weight


N = int(input_())
W = [int(input_()) for _ in range(N)]
P = [list(minput()) for _ in range(N)]
edges = []
for i in range(N):
    for j in range(i):
        edges.append((P[i][j], i, j))
for i in range(N):
    edges.append((W[i], i, N))

print(kruskal(N + 1, edges))
