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


def permutation_cycle_decomposition(l, permutation):
    processed = [False] * l
    for i in range(l):
        if processed[i]:
            continue
        pointer = i
        while not processed[pointer]:
            processed[pointer] = True
            uf.union(i, pointer)
            pointer = permutation[pointer]


n = int(input_())
friendship = [i for i in range(10000)]
uf = UnionFind(10000)
for _ in range(n):
    x, y = minput()
    friendship[x] = y
permutation_cycle_decomposition(10000, friendship)

while True:
    x, y = minput()
    if x ** 2 + y ** 2 == 0:
        break
    elif uf.find(x) != uf.find(y):
        print('No')
    else:
        ans = -1
        while x != y:
            ans += 1
            x = friendship[x]
        print('Yes', ans)
