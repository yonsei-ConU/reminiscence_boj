import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, x):
        self.parent = [i for i in range(x)]
        self.size = [1] * x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        elif self.size[root_x] >= self.size[root_y]:
            self.size[root_x] += self.size[root_y]
            self.parent[root_y] = root_x
        else:
            self.size[root_y] += self.size[root_x]
            self.parent[root_x] = root_y


def kruskal(v, edges):
    edges.sort()
    uf = UnionFind(v)
    mst_weight = 0
    max_weight = 0
    for edge in edges:
        weight, s, e, fuckyou = edge
        if uf.find(s) != uf.find(e):
            mst_weight += weight
            uf.union(s, e)
            max_weight = max(weight, max_weight)
    return mst_weight, max_weight


def notkruskal(v, edges, thres):
    mst_weight = 0
    mst = []
    uf = UnionFind(v)
    edges.sort(reverse=True)
    for w, u, v, fuckyou in edges:
        if w > thres:
            continue
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
            mst.append(fuckyou)
    return mst_weight, mst


print("NO")
N, M = minput()
edges = []
edges2 = [[] for _ in range(M + 1)]
for i in range(1, M + 1):
    u, v, w = minput()
    u -= 1; v -= 1
    edges.append((w, u, v, i))
    edges2[i] = [w, u, v]

mw, threshold = kruskal(N, edges)
mw2, mst = notkruskal(N, edges, threshold)
if mw == mw2:
    print("NO")
else:
    print("YES")
    for fuckyou in mst:
        print(fuckyou)
