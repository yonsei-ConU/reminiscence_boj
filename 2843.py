import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, x):
        self.parent = [i for i in range(x + 1)]
        self.x = x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            self.parent[root_x] = self.x
            self.parent[root_y] = self.x
        else:
            self.parent[root_x] = root_y


N = int(input_())
outgoing = list(map(lambda x: int(x) - 1, input_().split()))
output = []
queries = []
removed = [False] * N
for _ in range(int(input_())):
    query = list(minput())
    query[1] -= 1
    queries.append(query)
    if query[0] == 2:
        removed[query[1]] = True

for i in range(N):
    if not removed[i]:
        queries.append([2, i])

uf = UnionFind(N)
for q, v in queries[::-1]:
    if q == 1:
        root = uf.find(v)
        if root != N:
            output.append(str(root + 1))
        else:
            output.append("CIKLUS")
    else:
        if outgoing[v] != -1:
            uf.union(v, outgoing[v])

print('\n'.join(output[::-1]))
