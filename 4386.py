import sys
input_ = sys.stdin.readline
def minput(): return map(float, input().split())
from itertools import combinations as comb
from math import sqrt


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


def dist(a, b):
    assert len(a) == len(b)
    return sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


n = int(input_())
stars = [list(minput()) for _ in range(n)]
edges = []
for c in list(comb(range(n), 2)):
    star1 = stars[c[0]]
    star2 = stars[c[1]]
    edges.append((dist(star1, star2), c[0], c[1]))
    edges.append((dist(star1, star2), c[1], c[0]))

print(kruskal(n, edges))
