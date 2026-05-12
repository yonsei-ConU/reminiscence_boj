import sys
from collections import defaultdict
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


MOD = 1000000007
N = int(input_())
A = list(minput())
summation = lambda a, b: a + b
st = [segtree([0] * N, summation, 0) for _ in range(11)]
distinct = sorted(set(A))
rank = {distinct[i]: i for i in range(len(distinct))}
compressed = [rank[e] for e in A]
order = defaultdict(list)
for i in range(N)[::-1]: order[compressed[i]].append(i)

for v in range(len(distinct)):
    for idx in order[v]:
        st[0].update(idx, 1)
        for i in range(1, 11):
            to_add = st[i - 1].query(0, idx - 1)
            st[i].update(idx, (to_add + st[i].tree[st[i].n + idx]) % MOD)

print(st[10].query(0, N - 1) % MOD)
