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
    flowers = [tuple(minput()) for _ in range(N)]
    uf = UnionFind(2 * N)
    r_rev = {}
    c_rev = {}
    distinct = 0
    for r, c in flowers:
        if r not in r_rev:
            r_rev[r] = distinct
            distinct += 1
        if c not in c_rev:
            c_rev[c] = distinct
            distinct += 1
        uf.union(r_rev[r], c_rev[c])

    s = set()
    for r, c in flowers:
        s.add(uf.find(r_rev[r]))
    print(len(s) - 1)
