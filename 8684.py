import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


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


n, g = minput()
G = g
tickets = []
gsum = 0
for _ in range(n):
    w, p = minput()
    if not p:
        g -= w
        n -= 1
    else:
        gsum += w
        tickets.append((w, p))

if gsum < g:
    exit(print("NIE"))
elif g <= 0:
    exit(print(G))

dp = [float('inf')] * (g + 1)
dp[0] = 0

for w, p in tickets:
    st = segtree(dp, min, float('inf'))
    for j in range(g + 1)[::-1]:
        dp[j] = min(dp[j], p + st.query(max(0, j - w), j))

print(dp[-1] + G)
