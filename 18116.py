import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.ccsize = [1] * size

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
                self.ccsize[root_x] += self.ccsize[root_y]
                self.ccsize[root_y] = 0
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.ccsize[root_y] += self.ccsize[root_x]
                self.ccsize[root_x] = 0
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
                self.ccsize[root_x] += self.ccsize[root_y]
                self.ccsize[root_y] = 0


N = int(input_())
uf = UnionFind(1000000)
for _ in range(N):
    l = input_().split()
    l[1] = int(l[1]) - 1
    if l[0] == 'I':
        l[2] = int(l[2]) - 1
        uf.union(l[1], l[2])
    else:
        print(uf.ccsize[uf.find(l[1])])
