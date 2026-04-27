import io, os, __pypy__

reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
n, m, k = map(int, reader.readline().split())
arr = [int(reader.readline()) for _ in range(n)]
N = 1
while N < n:
    N <<= 1
tree = [0] * (N << 1)
for i in range(N):
    tree[N + i] = arr[i]
for i in range(N - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]
output = __pypy__.newlist_hint(m + k)
for i in range(m + k):
    a, b, c = map(int, reader.readline().split())
    if a == 1:
        b += N - 1
        tree[b] = c
        while b > 1:
            b >>= 1
            tree[b] = tree[2 * b] + tree[2 * b + 1]
    else:
        out = 0
        b += N - 1
        c += N - 1
        while b <= c:
            if b & 1:
                out += tree[b]
                b += 1
            if not c & 1:
                out += tree[c]
                c -= 1
            b >>= 1
            c >>= 1
        output.append(str(out))

os.write(1, '\n'.join(output).encode())
os._exit(0)
