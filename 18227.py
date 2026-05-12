import sys
sys.setrecursionlimit(234567)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class segtree:
    def __init__(self, arr, func, identity):
        i = 1
        while i < len(arr): i <<= 1
        self.n = i
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


def ETT(g, root):
    time = -1
    disc = [-1] * len(g)
    esc = [-1] * len(g)
    def ETT_process(cur, parent):
        nonlocal time
        time += 1
        disc[cur] = time
        for nxt in g[cur]:
            if nxt == parent:
                continue
            ETT_process(nxt, cur)
        esc[cur] = time
    ETT_process(root, -1)
    return disc, esc


def calcDepth(cur, parent):
    for nxt in g[cur]:
        if nxt == parent:
            continue
        depth[nxt] = depth[cur] + 1
        calcDepth(nxt, cur)


N, C = minput()
C -= 1
g = [[] for _ in range(N)]

for _ in range(N - 1):
    x, y = map(lambda x: int(x) - 1, input_().split())
    g[x].append(y)
    g[y].append(x)

depth = [1] * N
calcDepth(C, -1)
disc, esc = ETT(g, C)
st = segtree([0] * (N + 1), lambda a, b: a + b, 0)

for Q in range(int(input_())):
    query, city = list(minput())
    city -= 1
    if query == 1:
        cur = st.query(disc[city], disc[city])
        st.update(disc[city], cur + 1)
    else:
        print(st.query(disc[city], esc[city]) * depth[city])
