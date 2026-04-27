import sys
sys.setrecursionlimit(101010)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class segtree:
    def __init__(self, arr, func, identity):
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.tree = [identity] * (2 * self.n)
        self.func = func
        self.identity = identity
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        ret = self.identity
        l += self.n
        r += self.n
        while l <= r:
            if l % 2:
                ret = self.func(ret, self.tree[l])
                l += 1
            if not r % 2:
                ret = self.func(ret, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ret


def heavy_light_decomposition(graph, root):
    v = len(graph)
    sizes = [0] * v
    depth = [0] * v
    parent = [root] * v
    disc = [-1] * v
    esc = [-1] * v
    top = [root] * v
    time = -1
    g = [[] for _ in range(v)]

    def get_g(cur, par):
        for nxt in graph[cur]:
            if nxt == par:
                continue
            g[cur].append(nxt)
            get_g(nxt, cur)

    def decompose(cur):
        sizes[cur] = 1
        for nxt in g[cur]:
            depth[nxt] = depth[cur] + 1
            parent[nxt] = cur
            decompose(nxt)
            sizes[cur] += sizes[nxt]
        g[cur].sort(key=lambda x: sizes[x], reverse=True)

    def hld_ett(cur):
        nonlocal time
        time += 1
        disc[cur] = time
        for nxt in g[cur]:
            top[nxt] = top[cur] if nxt == g[cur][0] else nxt
            hld_ett(nxt)
        esc[cur] = time

    get_g(root, -1)
    decompose(root)
    hld_ett(root)

    return depth, parent, disc, top


class HLD_segtree:
    def __init__(self, st, graph, root):
        self.seg = st
        self.depth, self.parent, self.disc, self.top = heavy_light_decomposition(graph, root)

    def update(self, idx, val):
        self.seg.update(self.disc[idx], val)

    def query(self, l, r):
        ret = self.seg.identity
        while self.top[l] ^ self.top[r]:
            if self.depth[self.top[l]] < self.depth[self.top[r]]:
                l, r = r, l
            ret = self.seg.func(ret, self.seg.query(self.disc[self.top[l]], self.disc[l]))
            l = self.parent[self.top[l]]
        if self.depth[l] > self.depth[r]:
            l, r = r, l
        ret = self.seg.func(ret, self.seg.query(self.disc[l], self.disc[r]))
        return ret


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


N = int(input_())
uf_final = UnionFind(N)
uf_real = UnionFind(N)
penguins = list(minput())
g = [[] for _ in range(N)]
queries = []

for i in range(int(input_())):
    query = input_().split()
    x, y = int(query[1]), int(query[2])
    if query[0] == 'bridge':
        if uf_final.find(x - 1) != uf_final.find(y - 1):
            uf_final.union(x - 1, y - 1)
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        queries.append((1, x - 1, y - 1))
    elif query[0] == 'penguins':
        queries.append((2, x - 1, y))
    else:
        assert query[0] == 'excursion'
        queries.append((3, x - 1, y - 1))

for root in range(N):
    if g[root]:
        break
else:
    assert 0

for i in range(N):
    if uf_final.find(root) != uf_final.find(i):
        g[root].append(i)
        g[i].append(root)

st = segtree([0] * N, lambda a, b: a + b, 0)
hld = HLD_segtree(st, g, root)

for i in range(N):
    hld.update(i, penguins[i])

for q, x, y in queries:
    if q == 1:
        if uf_real.find(x) != uf_real.find(y):
            uf_real.union(x, y)
            print('yes')
        else:
            print('no')
    elif q == 2:
        hld.update(x, y)
    else:
        if uf_real.find(x) != uf_real.find(y):
            print('impossible')
        else:
            if x > y: x, y = y, x
            print(hld.query(x, y))
