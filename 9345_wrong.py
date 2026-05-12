import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def mult(a, b): return a * b % MOD


class segtree:
    """ConU's non-recursive uniform segment tree implementation"""
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


MOD = 998244353
for _ in range(int(input_())):
    N, K = minput()
    st = segtree(list(range(1, N + 1)), mult, 1)
    st_original = segtree(list(range(1, N + 1)), mult, 1)

    for i in range(K):
        Q, A, B = minput()
        if not Q:
            curA = st.query(A, A)
            curB = st.query(B, B)
            st.update(A, curB)
            st.update(B, curA)
        else:
            t1 = st.query(A, B)
            t2 = st_original.query(A, B)
            print('YNEOS'[t1 != t2::2])
