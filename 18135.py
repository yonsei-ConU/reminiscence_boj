import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='ascii')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


class lazy_segtree:
    def __init__(self, arr):
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.tree = [0] * (2 * self.n)
        self.lazy = [0] * (2 * self.n)
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def propagate(self, node, left, right):
        if self.lazy[node] != 0:
            self.tree[node] += (right - left + 1) * self.lazy[node]
            if left != right:
                for child in [2 * node, 2 * node + 1]:
                    self.lazy[child] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, l, r, add=0, node=1, left=0, right=None):
        if right is None:
            right = self.n - 1
        self.propagate(node, left, right)
        if r < left or right < l:
            return
        if l <= left and right <= r:
            self.lazy[node] += add
            self.propagate(node, left, right)
            return
        mid = (left + right) // 2
        self.update(l, r, add, 2 * node, left, mid)
        self.update(l, r, add, 2 * node + 1, mid + 1, right)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l, r, node=1, left=0, right=None):
        if right is None:
            right = self.n - 1
        self.propagate(node, left, right)
        if r < left or right < l:
            return 0
        if l <= left and right <= r:
            return self.tree[node]
        mid = (left + right) // 2
        p1 = self.query(l, r, 2 * node, left, mid)
        p2 = self.query(l, r, 2 * node + 1, mid + 1, right)
        return p1 + p2


output = []
N, M = minput()
districts = [-1] * N
arr = []
for x in range(M):
    a, b, c = minput()
    for i in range(a - 1, b):
        districts[i] = x
    arr.append(c)

st = lazy_segtree(arr)
while True:
    query = list(minput())
    if query == [0, 0, 0]:
        break
    elif query[0] == 1:
        x, y = query[1:]
        flag = x > y
        x = districts[x - 1]
        y = districts[y - 1]
        if flag and x == y:
            output.append(str(st.query(0, M - 1)))
        elif flag:
            output.append(str(st.query(x, M - 1) + st.query(0, y)))
        else:
            output.append(str(st.query(x, y)))
    elif query[0] == 2:
        x, y, z = query[1:]
        flag = x > y
        x = districts[x - 1]
        y = districts[y - 1]
        if flag and x == y:
            st.update(0, M - 1, add=z)
        elif flag:
            st.update(x, M - 1, add=z)
            st.update(0, y, add=z)
        else:
            st.update(x, y, add=z)

os.write(1, '\n'.join(output).encode())
os._exit(0)
