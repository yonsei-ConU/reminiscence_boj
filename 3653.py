import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


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
        ret_left = self.identity
        ret_right = self.identity
        l += self.n
        r += self.n
        while l <= r:
            if l & 1:
                ret_left = self.func(ret_left, self.tree[l])
                l += 1
            if not r & 1:
                ret_right = self.func(self.tree[r], ret_right)
                r -= 1
            l >>= 1
            r >>= 1
        return self.func(ret_left, ret_right)


for _ in range(int(input_())):
    n, m = minput()
    indices = list(range(m, m + n))
    st = segtree([0] * m + [1] * n, add, 0)
    query = list(minput())
    cur = m - 1
    ans = []
    for q in query:
        q -= 1
        ans.append(str(st.query(0, indices[q] - 1)))
        st.update(indices[q], 0)
        st.update(cur, 1)
        indices[q] = cur
        cur -= 1
    print(' '.join(ans))
