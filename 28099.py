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
        if l > r:
            return 0
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
    N = int(input_())
    A = list(minput())
    st = segtree(A, max, 0)
    rev = [[] for _ in range(N + 1)]
    for i in range(N):
        rev[A[i]].append(i)
    chk = True
    # print(rev)
    for i in range(N + 1):
        if len(rev[i]) >= 2:
            for j in range(len(rev[i]) - 1):
                if st.query(rev[i][j] + 1, rev[i][j + 1] - 1) > i:
                    chk = False
                    break
            if not chk:
                break
    if chk:
        print("Yes")
    else:
        print("No")
