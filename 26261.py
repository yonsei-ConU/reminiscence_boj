import sys
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


MAX = 500000
N, X, K = minput()
A = list(minput())

check = [False] * N
s = sum(A[:K])
if not s: check[K - 1] = True
ptr = K
while ptr < N:
    s += A[ptr]
    s -= A[ptr - K]
    if not s:
        check[ptr] = True
    ptr += 1

dp = [MAX] * N
st = segtree(dp[:], min, MAX)

for i in range(1, N - 1):
    if check[i]:
        if i - X < 0:
            dp[i] = 1
        else:
            dp[i] = st.query(i - X, i - K) + 1
        st.update(i, dp[i])

ans = st.query(max(0, N - X - 1), N - 1) + 1
print(ans if ans < MAX else -1)
