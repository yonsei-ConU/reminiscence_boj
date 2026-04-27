import sys
input_ = sys.stdin.readline
mod = 104857601
root = 3
def minput(): return map(int, input_().split())


def fft(arr, inverse=False):
    n = len(arr)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while not (j := j ^ bit) & bit:
            bit >>= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    length = 2
    while length <= n:
        omega = pow(root, (mod - 1) // length, mod)
        if inverse:
            omega = pow(omega, -1, mod)
        for i in range(0, n, length):
            w = 1
            for j in range(length // 2):
                u = arr[i + j]
                v = arr[i + j + length // 2] * w % mod
                arr[i + j] = (u + v) % mod
                arr[i + j + length // 2] = (u - v) % mod
                w = w * omega % mod
        length *= 2

    if inverse:
        inv_n = pow(n, -1, mod)
        arr = [(x * inv_n) % mod for x in arr]
    return arr


def conv(a, b):
    n = len(a) + len(b) - 1
    size = 1
    while size < n:
        size <<= 1
    a.extend([0] * (size - len(a)))
    b.extend([0] * (size - len(b)))
    a = fft(a)
    b = fft(b)
    c = [(a[i] * b[i]) % mod for i in range(size)]
    c = fft(c, True)
    return c[:n]


def divide_poly(f, g):
    F = f[::-1]
    G = g[::-1]
    H = [pow(G[0], -1, mod)]
    k = 1
    n = len(f)
    m = len(g)
    while k < n - m + 1:
        k <<= 1
        GH = conv(G[:], H[:])
        GH = [-x for x in GH]
        GH[0] += 2
        H = conv(H[:], GH[:])[:k]
    q = conv(F[:], H[:])[:n - m + 1][::-1]
    tmp = conv(g[:], q[:])
    r = []
    for i in range(max(len(f), len(tmp))):
        a = f[i] if i < len(f) else 0
        b = tmp[i] if i < len(tmp) else 0
        r.append((a - b) % mod)
    return r


def kitamasa(recurrence, A, N):
    assert len(recurrence) == len(A)
    N -= 1
    if N < len(A):
        return A[N]
    recurrence = [-x for x in recurrence] + [1]
    r = divide_poly([0] * N + [1], recurrence)
    return sum(A[i] * r[i] for i in range(len(A))) % mod


k, N = minput()
A = list(minput())
C = list(minput())
print(kitamasa(C[::-1], A, N))
