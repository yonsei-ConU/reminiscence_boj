import sys
from collections import defaultdict
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
        if l > r: return 0
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
data = defaultdict(int)
for _ in range(N):
    a, b = minput()
    data[a] += b

data2 = []
for v in sorted(data.keys()):
    data2.append([v, data[v]])
N = len(data2)
arts = []
for i in range(N - 1):
    arts += [data2[i][1] + data2[i][0] - data2[i + 1][0]]
arts += [data2[-1][1]]
psum = [0]
for i in range(len(arts)):
    psum.append(psum[-1] + arts[i])

st = segtree(psum, min, 10 ** 24)
ans = data2[0][1]
for end in range(1, N):
    ans = max(ans, data2[end][1] + max(0, psum[end] - st.query(0, end - 1)))

print(ans)
