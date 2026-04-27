import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.segments = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.segments -= 1
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
for _ in range(int(input_())):
    n, m, k, l = minput()
    uf = UnionFind(n * m * k)
    queries = []
    enabled = [True] * (n * m * k)
    not_enabled = 0
    for i in range(l):
        a, *b = minput()
        queries.append(b)
        for c in b:
            enabled[c] = False
            not_enabled += 1
    queries.append([i for i in range(n * m * k) if enabled[i]])
    ans = l

    while queries:
        q = queries.pop()
        for point in q:
            enabled[point] = True
            not_enabled -= 1
            z = point // (n * m)
            y = point % (n * m) // n
            x = point % n
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < k and enabled[nx + ny * n + nz * n * m]:
                    uf.union(point, nx + ny * n + nz * n * m)
        if len(set(uf.find(i) for i in range(n * m * k) if enabled[i])) != 1:
            ans = len(queries)
    print(ans + 1 if ans != l else 0)
