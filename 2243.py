import sys
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


n = int(input_())
st = segtree([0] * 10 ** 6, lambda a, b: a + b, 0)

for _ in range(n):
    l = list(minput())
    if l[0] == 1:
        lo = -1
        hi = 10 ** 6
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if st.query(0, mid) >= l[1]:
                hi = mid
            else:
                lo = mid
        res = hi
        print(hi + 1)
        st.update(hi, st.tree[res + 2 ** 20] - 1)
    else:
        flavor, delta = l[1:]
        flavor -= 1
        current_amount = st.tree[flavor + 2 ** 20]
        st.update(flavor, current_amount + delta)
