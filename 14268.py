import sys
sys.setrecursionlimit(100000)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def euler_tour_technique(cur, parent):
    """
    predefine
    time = 0
    disc = [-1] * len(g)
    esc = [-1] * len(g)
    나는 disc[i]
    내 서브트리는 disc[i] 부터 esc[i]
    """
    global time
    time += 1
    disc[cur] = time
    for nxt in g[cur]:
        if nxt == parent:
            continue
        euler_tour_technique(nxt, cur)
    esc[cur] = time


class segtree_zero:
    def __init__(self, n, func, identity):
        self.n = 1
        while self.n < n: self.n <<= 1
        self.tree = [identity] * (2 * self.n)
        self.func = func
        self.identity = identity

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


n, m = minput()
g = [[] for _ in range(n)]
tkdtk = list(minput())
for i in range(1, n):
    g[i].append(tkdtk[i] - 1)
    g[tkdtk[i] - 1].append(i)

disc = [-1] * n
esc = [-1] * n
time = -1
euler_tour_technique(0, -1)
st = segtree_zero(n + 1, lambda a, b: a + b, 0)

for _ in range(m):
    query = list(minput())
    if query[0] == 1:
        i, w = query[1:]
        i -= 1
        tmp = st.query(disc[i], esc[i])
        st.update(disc[i], tmp + w)
        st.update(esc[i] + 1, tmp - w)
    else:
        i = query[1]
        print(st.query(disc[i - 1], esc[i - 1]))
