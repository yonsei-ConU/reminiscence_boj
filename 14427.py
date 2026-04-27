import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cmp(a, b):
    if a[1] > b[1]:
        return b
    elif a[1] < b[1]:
        return a
    else:
        if a[0] < b[0]:
            return a
        return b


class segtree:
    def __init__(self, arr, func, identity):
        i = 1
        while i < len(arr): i <<= 1
        self.n = i
        self.tree = [identity] * (2 * self.n)
        self.func = func
        self.identity = identity
        for i in range(len(arr)):
            self.tree[self.n + i] = (i, arr[i])
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = (idx - self.n, val)
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


N = int(input_())
A = list(minput())
st = segtree(A, cmp, (123123, 10 ** 9 + 2))

for _ in range(int(input_())):
    query = list(minput())
    if query[0] == 1:
        st.update(query[1] - 1, query[2])
    else:
        print(st.query(0, N - 1)[0] + 1)
