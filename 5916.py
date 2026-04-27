import sys
from types import GeneratorType
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


def bootstrap(f, stack=[]):
    from types import GeneratorType
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


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

    @bootstrap
    def get_g(cur, par):
        for nxt in graph[cur]:
            if nxt == par:
                continue
            g[cur].append(nxt)
            yield get_g(nxt, cur)
        yield

    @bootstrap
    def decompose(cur):
        sizes[cur] = 1
        max_size = 0
        max_idx = 0
        for i in range(len(g[cur])):
            nxt = g[cur][i]
            depth[nxt] = depth[cur] + 1
            parent[nxt] = cur
            yield decompose(nxt)
            sizes[cur] += sizes[nxt]
            if sizes[nxt] > max_size:
                max_size = sizes[nxt]
                max_idx = i
        if g[cur]:
            g[cur][0], g[cur][max_idx] = g[cur][max_idx], g[cur][0]
        yield

    @bootstrap
    def hld_ett(cur):
        nonlocal time
        time += 1
        disc[cur] = time
        for nxt in g[cur]:
            top[nxt] = top[cur] if nxt == g[cur][0] else nxt
            yield hld_ett(nxt)
        esc[cur] = time
        yield

    get_g(root, -1)
    decompose(root)
    hld_ett(root)

    return depth, parent, disc, top


class lazy_segtree:
    """only lazy sum seg"""
    def __init__(self, arr):
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.tree = [0] * (2 * self.n)
        self.lazy = [0] * (2 * self.n)
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def propagate(self, node, left, right):
        if self.lazy[node] != 0:
            self.tree[node] += (right - left + 1) * self.lazy[node]
            if left != right:
                for child in [2 * node, 2 * node + 1]:
                    self.lazy[child] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, l, r, add=1, node=1, left=0, right=None):
        if right is None:
            right = self.n - 1
        self.propagate(node, left, right)
        if r < left or right < l:
            return
        if l <= left and right <= r:
            self.lazy[node] += add
            self.propagate(node, left, right)
            return
        mid = (left + right) // 2
        self.update(l, r, add, 2 * node, left, mid)
        self.update(l, r, add, 2 * node + 1, mid + 1, right)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

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
        return p1 + p2


def path_update(u, v):
    while top[u] ^ top[v]:
        if depth[top[u]] < depth[top[v]]:
            u, v = v, u
        st.update(disc[top[u]], disc[u])
        u = parent[top[u]]
    if depth[u] > depth[v]:
        u, v = v, u
    st.update(disc[u] + 1, disc[v])


def path_query(u, v):
    ret = 0
    while top[u] ^ top[v]:
        if depth[top[u]] < depth[top[v]]:
            u, v = v, u
        ret += st.query(disc[top[u]], disc[u])
        u = parent[top[u]]
    if depth[u] > depth[v]:
        u, v = v, u
    ret += st.query(disc[u] + 1, disc[v])
    return ret


N, M = minput()
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = minput()
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

depth, parent, disc, top = heavy_light_decomposition(g, 0)
st = lazy_segtree([0] * N)

for _ in range(M):
    w, u, v = input_().split()
    u = int(u) - 1
    v = int(v) - 1
    if w == 'P':
        path_update(u, v)
    else:
        print(path_query(u, v))
