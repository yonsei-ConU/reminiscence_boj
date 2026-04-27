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


def coordinate_compression(lst):
    distinct = sorted(set(lst))
    rank = {distinct[i]: i for i in range(len(distinct))}
    return rank


N, X = minput()
if N == 1: exit(print(0))
H = list(minput())
lo = -1
hi = max(H) - min(H) + 1

while lo + 1 < hi:
    mid = (lo + hi) >> 1
    H_mid = []
    for h in H:
        H_mid.extend([h, h - mid, h + mid])
    rank = coordinate_compression(H_mid)

    st = segtree_zero(len(rank), max, 0)
    dp = [0] * N
    for i in range(N):
        cur_h = rank[H[i]]
        l, r = rank[H[i] - mid], rank[H[i] + mid]
        max_prev = st.query(l, r)
        dp[i] = max_prev + 1
        st.update(cur_h, dp[i])

        if dp[i] >= X:
            hi = mid
            break
    else:
        lo = mid

print(hi)
