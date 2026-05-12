import sys
input_ = sys.stdin.readline
sys.setrecursionlimit(202020)
def minput(): return map(int, input_().split())
def min_(a, b): return b if a > b else a


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


class segtree:
    def __init__(self, arr, func, identity):
        i = 1
        while i < len(arr): i <<= 1
        self.n = i
        self.tree = [identity for _ in range(2 * self.n)]
        self.func = func
        self.identity = identity
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

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
            if l & 1:
                ret = self.func(self.tree[l], ret)
                l += 1
            if not r & 1:
                ret = self.func(ret, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ret


class HLD_segtree:
    def __init__(self, st, graph, root):
        self.seg = st
        self.sizes, self.depth, self.parent, self.disc, self.esc, self.top = heavy_light_decomposition(graph, root)

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
        ret = self.seg.func(ret, self.seg.query(self.disc[l] + 1, self.disc[r]))
        return ret


N, Q = minput()
g = [[] for _ in range(N)]

for i in range(1, N):
    par = int(input_()) - 1
    g[i].append(par)
    g[par].append(i)

sizes, depth, parent, disc, esc, top = heavy_light_decomposition(g, 0)
st = segtree([1] * N, min_, 1)
hld = HLD_segtree(st, g, 0)

for i in range(Q):
    b, c, d_ = minput()
    b -= 1; c -= 1
    path_min = hld.query(b, c)
    if path_min:
        print('YES')
        if d_:
            hld.update(b, 0)
    else:
        print('NO')
        if d_:
            hld.update(c, 0)
