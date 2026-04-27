import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def merge(A, B): return [A[0] + B[0], max(A[0] + B[1], A[1]), max(B[0] + A[2], B[2]), max(A[3], B[3], A[2] + B[1])]


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
goldmine = []
X = set()
Y = set()
for _ in range(N):
    x, y, w = minput()
    X.add(x)
    Y.add(y)
    goldmine.append((x, y, w))

X = sorted(X)
Y = sorted(Y)
X_rank = {X[i]: i for i in range(len(X))}
Y_rank = {Y[i]: i for i in range(len(Y))}

goldmine.sort()
ans = 0
identity = [0, -10 ** 18, -10 ** 18, -10 ** 18]

for i in range(N):
    if i and goldmine[i - 1][0] == goldmine[i][0]:
        continue
    st = segtree([identity for _ in range(len(Y))], merge, identity)
    for j in range(i, N):
        st.update(Y_rank[goldmine[j][1]], [goldmine[j][2] + st.query(Y_rank[goldmine[j][1]], Y_rank[goldmine[j][1]])[0]] * 4)
        if j == N - 1 or goldmine[j][0] != goldmine[j + 1][0]:
            ans = max(ans, st.tree[1][3])

print(ans)
