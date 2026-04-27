import sys
from collections import defaultdict
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


for _ in range(int(input_())):
    N = int(input_())
    X = defaultdict(list)
    Y = defaultdict(list)
    for i in range(N):
        x, y = minput()
        X[x].append(i)
        Y[y].append(i)

    uf = UnionFind(N)
    for lst in X.values():
        if len(lst) == 1: continue
        for v in lst[1:]:
            uf.union(v, lst[0])
    for lst in Y.values():
        if len(lst) == 1: continue
        for v in lst[1:]:
            uf.union(v, lst[0])

    components = len(set([uf.find(i) for i in range(N)]))
    print((components + 1) >> 1)
