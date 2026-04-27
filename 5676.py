import sys
from math import ceil, log2
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

def sgn(x):
    if x == 0:
        return 0
    return x / abs(x)

class segtree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0]*(1 << (ceil(log2(len(arr))) + 1))
        self.build(1, 0, len(arr)-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start+end)//2
            self.build(2*node, start, mid)
            self.build(2*node+1, mid+1, end)
            self.tree[node] = sgn(self.tree[2*node] * self.tree[2*node+1])

    def update(self, node, start, end, idx, val):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
        else:
            mid = (start+end)//2
            if start <= idx and idx <= mid:
                self.update(2*node, start, mid, idx, val)
            else:
                self.update(2*node+1, mid+1, end, idx, val)
            self.tree[node] = sgn(self.tree[2*node] * self.tree[2*node+1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 1
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start+end)//2
        p1 = self.query(2*node, start, mid, l, r)
        p2 = self.query(2*node+1, mid+1, end, l, r)
        return sgn(p1 * p2)


while 69:
    try:
        N, K = minput()
    except EOFError:
        exit()
    ans = ''
    X = list(map(lambda x: sgn(int(x)), input_().split()))
    st = segtree(X)
    for _ in range(K):
        cmd = input_().split()
        if cmd[0] == 'C':
            i, V = int(cmd[1]), int(cmd[2])
            st.update(1, 0, N-1, i-1, V)
        else:
            i, j = int(cmd[1]), int(cmd[2])
            sign = st.query(1, 0, N-1, i-1, j-1)
            if sign == 0:
                ans += '0'
            elif sign > 0:
                ans += '+'
            else:
                ans += '-'
    print(ans)
