import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


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


msz = 1200001
n = int(input_())
st = segtree([0] * msz, lambda a, b: a + b, 0)
frogs = list(minput())
for f in frogs:
    st.update(f, 1)

for _ in range(int(input_())):
    i = int(input_()) - 1
    cur = frogs[i]
    lo = cur
    hi = msz
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if st.query(cur + 1, mid) == mid - cur:
            lo = mid
        else:
            hi = mid
    print(hi)
    st.update(cur, 0)
    st.update(hi, 1)
    frogs[i] = hi
