import sys
input_ = sys.stdin.readline
sys.setrecursionlimit(505050)
def minput(): return map(int, input_().split())


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

    return sizes, depth, parent, disc, esc, top


class lazy_segtree:
    def __init__(self, arr):
        self.mod = 1 << 32
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.tree = [0] * (2 * self.n)
        self.lazy_add = [0] * (2 * self.n)
        self.lazy_mul = [1] * (2 * self.n)
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i] % self.mod
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = (self.tree[2 * i] + self.tree[2 * i + 1]) % self.mod

    def propagate(self, node, left, right):
        if self.lazy_mul[node] != 1 or self.lazy_add[node] != 0:
            self.tree[node] = (self.tree[node] * self.lazy_mul[node] + (right - left + 1) * self.lazy_add[node]) % self.mod
            if left != right:
                for child in [2 * node, 2 * node + 1]:
                    self.lazy_mul[child] = (self.lazy_mul[child] * self.lazy_mul[node]) % self.mod
                    self.lazy_add[child] = (self.lazy_add[child] * self.lazy_mul[node] + self.lazy_add[node]) % self.mod
            self.lazy_mul[node] = 1
            self.lazy_add[node] = 0

    def update(self, l, r, add=0, mul=1, node=1, left=0, right=None):
        if right is None:
            right = self.n - 1
        self.propagate(node, left, right)
        if r < left or right < l:
            return
        if l <= left and right <= r:
            self.lazy_mul[node] = (self.lazy_mul[node] * mul) % self.mod
            self.lazy_add[node] = (self.lazy_add[node] * mul + add) % self.mod
            self.propagate(node, left, right)
            return
        mid = (left + right) // 2
        self.update(l, r, add, mul, 2 * node, left, mid)
        self.update(l, r, add, mul, 2 * node + 1, mid + 1, right)
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.mod

    def query(self, l, r, node=1, left=0, right=None):
        if right is None:
            right = self.n - 1
        self.propagate(node, left, right)
        if r < left or right < l:
            return 0
        if l <= left and right <= r:
            return self.tree[node]
        mid = (left + right) // 2
        p1 = self.query(l, r, 2 * node, left, mid)
        p2 = self.query(l, r, 2 * node + 1, mid + 1, right)
        return (p1 + p2) % self.mod


class HLD_segtree:
    def __init__(self, st, graph, root):
        self.seg = st
        self.sizes, self.depth, self.parent, self.disc, self.esc, self.top = heavy_light_decomposition(graph, root)

    def add(self, u, v, val):
        while self.top[u] != self.top[v]:
            if self.depth[self.top[u]] < self.depth[self.top[v]]:
                u, v = v, u
            self.seg.update(self.disc[self.top[u]], self.disc[u], add=val)
            u = self.parent[self.top[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        self.seg.update(self.disc[u], self.disc[v], add=val)

    def mult(self, u, v, val):
        while self.top[u] != self.top[v]:
            if self.depth[self.top[u]] < self.depth[self.top[v]]:
                u, v = v, u
            self.seg.update(self.disc[self.top[u]], self.disc[u], mul=val)
            u = self.parent[self.top[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        self.seg.update(self.disc[u], self.disc[v], mul=val)

    def query(self, u, v):
        ret = 0
        while self.top[u] != self.top[v]:
            if self.depth[self.top[u]] < self.depth[self.top[v]]:
                u, v = v, u
            ret = (ret + self.seg.query(self.disc[self.top[u]], self.disc[u])) % self.seg.mod
            u = self.parent[self.top[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        ret = (ret + self.seg.query(self.disc[u], self.disc[v])) % self.seg.mod
        return ret


N, Q = minput()
g = [[] for _ in range(N)]

for _ in range(N - 1):
    S, E = minput()
    S -= 1; E -= 1
    g[S].append(E)
    g[E].append(S)

hld = HLD_segtree(lazy_segtree([0] * N), g, 0)

for _ in range(Q):
    query = list(minput())

    if query[0] == 1:
        X, V = query[1:]
        hld.seg.update(hld.disc[X - 1], hld.esc[X - 1], add=V)

    elif query[0] == 2:
        X, Y, V = query[1:]
        hld.add(X - 1, Y - 1, V)

    elif query[0] == 3:
        X, V = query[1:]
        hld.seg.update(hld.disc[X - 1], hld.esc[X - 1], mul=V)

    elif query[0] == 4:
        X, Y, V = query[1:]
        hld.mult(X - 1, Y - 1, V)

    elif query[0] == 5:
        X = query[1]
        print(hld.seg.query(hld.disc[X - 1], hld.esc[X - 1]))

    elif query[0] == 6:
        X, Y = query[1:]
        print(hld.query(X - 1, Y - 1))
