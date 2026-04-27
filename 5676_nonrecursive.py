import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

def sgn(x):
    if x == 0:
        return 0
    return x / abs(x)

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


while 69:
    try:
        N, K = minput()
    except:
        exit()
    if N == 0:
        exit()
    ans = ''
    X = list(map(lambda x: sgn(int(x)), input_().split()))
    st = segtree(X, lambda a, b: sgn(a * b), 1)
    for _ in range(K):
        cmd = input_().split()
        if cmd[0] == 'C':
            i, V = int(cmd[1]), int(cmd[2])
            st.update(i-1, V)
        else:
            i, j = int(cmd[1]), int(cmd[2])
            sign = st.query(i-1, j-1)
            if sign == 0:
                ans += '0'
            elif sign > 0:
                ans += '+'
            else:
                ans += '-'
    print(ans)
