import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


class segtree:
    """ConU's non-recursive uniform segment tree implementation"""
    def __init__(self, arr, func, identity):
        i = 1
        while i < len(arr): i <<= 1
        self.n = i
        self.tree = [identity for _ in range(self.n << 1)]
        self.func = func
        self.identity = identity
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[i << 1], self.tree[(i << 1) | 1])

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[idx << 1], self.tree[(idx << 1) | 1])

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


MOD = 10 ** 9 + 7
N = int(input_())
factorial_mod = [1, 1]
for i in range(2, N + 1):
    factorial_mod.append(factorial_mod[-1] * i % MOD)
P = list(minput())
s = sorted(P)
rank = {s[i]: i for i in range(N)}
newP = [rank[e] + 1 for e in P]
st = segtree([1] * (N + 1), add, 0)
st.update(0, 0)
ans = 0

for i in range(N):
    ans = (ans + st.query(0, newP[i] - 1) * factorial_mod[N - 1 - i]) % MOD
    st.update(newP[i], 0)

print((ans + 1) % MOD)
