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

    return sizes, depth, parent, disc, esc, top


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


def find_par(cur, par):
    for nxt in g[cur]:
        if nxt == par:
            continue
        parent[nxt] = cur
        find_par(nxt, cur)


N = int(input_())
g = [[] for _ in range(N)]
g2 = [{} for _ in range(N)]
edges = []

for _ in range(N - 1):
    u, v, w = minput()
    u -= 1; v -= 1
    g[u].append(v)
    g[v].append(u)
    g2[u][v] = g2[v][u] = w
    edges.append((u, v))

parent = [0] * N
find_par(0, 0)

arr = [0] * N
edge_child = [0] * (N - 1)

for i in range(N):
    if i: arr[i] = g2[i][parent[i]]
    if i != N - 1:
        if parent[edges[i][0]] == edges[i][1]:
            edge_child[i] = edges[i][0]
        else:
            edge_child[i] = edges[i][1]

st = segtree([0] * N, min, 2000000)
hld = HLD_segtree(st, g, 0)
st2 = segtree([0] * N, max, 0)
hld2 = HLD_segtree(st2, g, 0)

for i in range(N):
    hld.update(i, arr[i])
    hld2.update(i, arr[i])

q = int(input_())
for _ in range(q):
    d, e = minput()
    if d == e:
        print('0 0')
    else:
        print(hld.query(d - 1, e - 1), hld2.query(d - 1, e - 1))
