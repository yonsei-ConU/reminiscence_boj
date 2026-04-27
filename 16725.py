import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def fft(arr, mod, root, inverse=False):
    root = 5
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


def conv(a, b, mod, root):
    a = a[:]
    b = b[:]
    n = len(a) + len(b) - 1
    size = 1
    while size < n:
        size <<= 1
    a.extend([0] * (size - len(a)))
    b.extend([0] * (size - len(b)))
    a = fft(a, mod, root)
    b = fft(b, mod, root)
    c = [(a[i] * b[i]) % mod for i in range(size)]
    c = fft(c, mod, root, True)[:n]
    while c and not c[-1]:
        c.pop()
    return c


def egcd(a, b):
    if not b:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def crt(remainders, mods):
    x = 1
    for m in mods:
        x *= m

    ret = 0
    for m, r in zip(mods, remainders):
        t = x // m
        ret += r * t * pow(t, -1, m)

    return ret % x


def poly_mult(base, exponent, mod, root):
    ret = [1] + [0] * n
    while exponent:
        if exponent & 1:
            ret = conv(ret, base, mod, root)
        exponent >>= 1
        base = conv(base, base, mod, root)
    return ret


MOD = 10 ** 9 + 9
n, m, k = minput()
p1 = poly_mult([1] * (n + 1), m, 3221225473, 5)
p2 = poly_mult([1] * (n + 1), m, 2281701377, 3)
p3 = poly_mult([1] * (n + 1), m, 2013265921, 31)
p4 = poly_mult([1] * (n + 1), m, 998244353, 3)
x = crt([p1[k], p2[k]], [3221225473, 2281701377])
x = crt([x, p3[k]], [3221225473*2281701377, 2013265921])
print(x % MOD)
