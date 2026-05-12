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
l = [[], [], []]
X, Y, Z = l
for i in range(N):
    x, y, z = minput()
    X.append((x, y, z, i))
    Y.append((y, z, x, i))
    Z.append((z, x, y, i))

edges = []
X.sort(); Y.sort(); Z.sort()
for i in range(N - 1):
    for j in range(3):
        cur = l[j][i]
        nxt = l[j][i + 1]
        dist = min(abs(nxt[z] - cur[z]) for z in range(3))
        edges.append((dist, nxt[3], cur[3]))

print(kruskal(N, edges))
