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


for _ in range(int(input_())):
    F = int(input_())
    uf = UnionFind(2 * F)
    v = {}
    for i in range(F):
        p1, p2 = input_().rstrip().split()
        if p1 in v:
            x1 = v[p1]
        else:
            x1 = len(v)
            v[p1] = x1
        if p2 in v:
            x2 = v[p2]
        else:
            x2 = len(v)
            v[p2] = x2
        uf.union(x1, x2)
        print(uf.size[uf.find(x1)])
