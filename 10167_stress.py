import sys
from random import randint
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


def naive():
    gm2 = [[0] * len(X) for _ in range(len(Y))]
    for i in range(N):
        x, y, w = goldmine[i]
        x = X_rank[x]
        y = Y_rank[y]
        gm2[y][x] = w

    ps = [[0] * len(X)]
    for i in range(len(Y)): ps.append([ps[-1][j] + gm2[i][j] for j in range(len(X))])

    ans = 0
    for i in range(1, len(Y) + 1):
        for j in range(i):
            lst = [[ps[i][k] - ps[j][k]] * 4 for k in range(len(X))]
            ans = max(ans, segtree(lst, merge, [0, -10 ** 18, -10 ** 18, -10 ** 18]).tree[1][-1])
    return ans


def solve():
    goldmine.sort()
    ans2 = 0
    identity = [0, -10 ** 18, -10 ** 18, -10 ** 18]

    for i in range(N):
        if i and goldmine[i - 1][0] == goldmine[i][0]:
            continue
        st = segtree([identity for _ in range(len(Y))], merge, identity)
        for j in range(i, N):
            st.update(Y_rank[goldmine[j][1]], [goldmine[j][2] + st.query(Y_rank[goldmine[j][1]], Y_rank[goldmine[j][1]])[0]] * 4)
            if j == N - 1 or goldmine[j][0] != goldmine[j + 1][0]:
                ans2 = max(ans2, st.tree[1][3])

    return ans2


for tc in range(1, 10001):
    N = 3
    goldmine = []
    X = set()
    Y = set()
    validator = set()
    cnt = 0
    while cnt < N:
        x = randint(0, N + 1)
        y = randint(0, N + 1)
        w = randint(-10, 10)
        if (x, y) in validator:
            continue
        X.add(x)
        Y.add(y)
        validator.add((x, y))
        goldmine.append((x, y, w))
        cnt += 1

    X = sorted(X)
    Y = sorted(Y)
    X_rank = {X[i]: i for i in range(len(X))}
    Y_rank = {Y[i]: i for i in range(len(Y))}

    n = naive()
    s = solve()
    if n != s:
        print(f'TC {tc} failed')
        print()
        print(N)
        for gm in goldmine: print(*gm)
        print()
        print(f'naive answer {n}, solve answer {s}')
        break
else:
    print('10000 TC passed')
"""
+0 +0 +0 +8
+0 +0 +0 +0
+5 +0 +0 -6
"""