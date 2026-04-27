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


N, Q = minput()
A = list(minput())
st = segtree(A * 2, lambda a, b: a + b, 0)
pos = 0

for _ in range(Q):
    query = list(minput())
    if query[0] == 1:
        query[1] -= 1
        cur = st.query(query[1], query[1])
        st.update(query[1], cur ^ 1)
        st.update(query[1] + N, cur ^ 1)
    elif query[0] == 2:
        pos = (pos + query[1]) % N
    else:
        l, r = pos, 2 * N - 1
        answer = -1
        while l + 1 < r:
            mid = (l + r) // 2
            if st.query(pos, mid) > 0:
                answer = mid
                r = mid
            else:
                l = mid
        if answer == -1:
            print(-1)
        else:
            print(answer - pos)
        
