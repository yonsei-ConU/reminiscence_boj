import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


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


def coordinate_compression(lst):
    distinct = sorted(set(lst))
    rank = {distinct[i]: i for i in range(len(distinct))}
    return rank


# 1D, M is unnecessary
for _ in range(int(input_())):
    N, M, x = minput()
    mat = list(minput())
    ps = []
    ps_x = []
    cur_sum = 0
    ans = 0
    for i in range(N):
        cur_sum += mat[i]
        if mat[i] <= x: ans += 1
        ps.append(cur_sum)
        ps_x.extend([cur_sum, cur_sum + x])
    ps_rank = coordinate_compression(ps_x)
    st = segtree_zero(2 * N, lambda a, b: a + b, 0)
    for i in range(N):
        ans += st.query(ps_rank[ps[i]], 2 * N - 1)
        st.update(ps_rank[ps[i] + x], st.tree[st.n + ps_rank[ps[i] + x]] + 1)
    print(ans)
