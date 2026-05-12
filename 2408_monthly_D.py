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


N, M, K = minput()
ruby = [list(minput()) for _ in range(N)]
# dp[i][k][j] = (ruby[i]까지 검사 완료, 마지막으로 j번째에서 먹음, 여태까지 k개만큼 먹음
dp = [[[0] * M for _ in range(K + 1)] for _ in range(N)]
for j in range(M): dp[0][1][j] = ruby[0][j]

for i in range(1, N):
    for k in range(K):
        st = segtree(dp[i][k], max, -1)
        for j in range(M):
            m = -1
            if j:
                m = max(m, st.query(0, j - 1))
            if j != M - 1:
                m = max(m, st.query(j + 1, M - 1))
            dp[i][k][j] = max(dp[i - 1][k][j], m + ruby[i][j])

ans = 0
for k in range(K):
    ans = max(ans, max(dp[-1][k]))

print(ans)
"""3 3 1
1 9 1
3 9 3
9 1 3"""