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


N = int(input_())
A = list(minput())
st1 = segtree([0] * N, add, 0)
st2 = segtree([0] * N, add, 0)

for _ in range(int(input_())):
    query = list(minput())
    if query[0] == 1:
        left = int(query[1]) - 1
        right = int(query[2]) - 1
        st1.update(left, N - left + st1.tree[st1.n + left])
        st2.update(left, 1 + st2.tree[st2.n + left])
        if right + 1 < N:
            st1.update(right + 1, st1.tree[st1.n + right + 1] - (right - left + 2) * (N - right - 1))
            st2.update(right + 1, st2.tree[st2.n + right + 1] - (right - left + 2))
        if right + 2 < N:
            st1.update(right + 2, st1.tree[st1.n + right + 2] + (right - left + 1) * (N - right - 2))
            st2.update(right + 2, st2.tree[st2.n + right + 2] + (right - left + 1))
    else:
        idx = int(query[1]) - 1
        print(st1.query(0, idx) - st2.query(0, idx) * (N - 1 - idx) + A[idx])
    # print(st1.tree[st1.n:st1.n+10])
    # print(st2.tree[st2.n:st2.n+10])
    # print()
