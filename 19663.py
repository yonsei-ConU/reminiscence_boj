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


n = int(input_())
H = list(minput())
indexed_H = [(value, index) for index, value in enumerate(H)]

indexed_H.sort()

P = []
current_group = []
current_value = None

for value, index in indexed_H:
    if value != current_value:
        if current_group:
            P.append(current_group if len(current_group) > 1 else current_group[0])
        current_group = [index]
        current_value = value
    else:
        current_group.append(index)

if current_group:
    P.append(current_group if len(current_group) > 1 else current_group[0])

st = segtree([0] * n, lambda a, b: a + b, 0)
ans = 0
for i in range(len(P)):
    if isinstance(P[i], int): P[i] = [P[i]]
    for element in P[i]:
        if element:
            a = st.query(0, element - 1)
        else:
            a = 0
        if element != n - 1:
            b = st.query(element + 1, n - 1)
        else:
            b = 0
        ans += a * b
    for element in P[i]:
        st.update(element, 1)

print(ans)
